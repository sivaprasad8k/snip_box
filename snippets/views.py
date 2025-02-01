import datetime
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from core.enums import Response
from core.exceptions import manage_exception, DataFetchFailedException
from core.functions import generate_response
from .models import Snippet, Tag
from .serializers import SnippetSerializer, SnippetDetailSerializer
from .service import format_data, get_snippet_data


class RegenerateTokenView(APIView):
    permission_classes = []  # Ensure the user is logged in.

    def post(self, request, *args, **kwargs):
        user = request.user  # Get the logged-in user

        # If you have username/password, you can regenerate like this:
        user = User.objects.get(username='sivaprasad')

        # Generate refresh token and access token for the user
        refresh = RefreshToken.for_user(user)

        # You can return both access and refresh tokens
        return generate_response(Response.DataFound, {'access': str(refresh.access_token), 'refresh': str(refresh)})


@api_view(['GET'])
def snippet_list(request):
    snippets = Snippet.objects.all()
    snippet_count = snippets.count()
    serializer = SnippetDetailSerializer(snippets, many=True)

    return generate_response(Response.DataFound, {"total_snippets": snippet_count, "snippets": serializer.data})


class Snippets(APIView):
    """ API for performing CRUD operation on Snippets """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        """ Method for getting whole or individual snippet """
        try:
            filter_dict = {'created_by': request.user} if not pk else {'id': pk}
            result = Snippet.objects.filter(**filter_dict).values('id', 'note', 'created_at',
                                                                  created=F('created_by__username'),
                                                                  title=F('tag__title'))
            if not result.exists():
                raise DataFetchFailedException
            final_data = generate_response(Response.DataFound, format_data(result))
        except Exception as ex:
            final_data = manage_exception(ex)

        return final_data

    def post(self, request):
        """
        Method for creating new snippet. if already have a title then take the pk of title and save it on snippet
        else create a new one and save its pk to snippet"""
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            with transaction.atomic():
                tag, created = Tag.objects.get_or_create(title=data.pop('title'))
                Snippet.objects.create(tag_id=tag.id, **{**data, **{'created_by': request.user}})
            final_data = generate_response(Response.DataSaved)
        else:
            final_data = generate_response(Response.ValidationError, serializer.errors)

        return final_data

    def put(self, request):
        """ Method for updating existing snippet """
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            id = data.pop('id')
            with transaction.atomic():
                tag, created = Tag.objects.get_or_create(title=data.pop('title'))
                data.update({'tag_id': tag.id, 'updated_at': datetime.datetime.now()})
                Snippet.objects.filter(pk=id).update(**data)
                result = get_snippet_data({'id': id})
            final_data = generate_response(Response.DataUpdated, result)
        else:
            final_data = generate_response(Response.ValidationError, serializer.errors)

        return final_data

    def delete(self, request, pk):
        """ Method for deleting existing Grade """
        Snippet.objects.filter(pk=pk).delete()
        result = get_snippet_data({})

        return generate_response(Response.DataDeleted, result)


@api_view(['GET'])
def tags(request, id=None):
    """ Method for getting tags, if tag id passed return snippets belong to the tag """
    try:
        if id:
            result = get_snippet_data({'tag_id': id} if id else {})
        else:
            result = list(Tag.objects.all().values())
        final_data = generate_response(Response.DataFound, result)
    except Exception as Ex:
        final_data = manage_exception(Ex)

    return final_data
