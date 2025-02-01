from rest_framework import serializers

from core.functions import change_date_format
from .models import Snippet, Tag

from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Snippet




class SnippetDetailSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Snippet
        fields = ['id', 'note', 'created_at', 'updated_at', 'detail_url']

    def to_representation(self, instance):
        # Add a custom field (e.g., snippet_age) based on the created_at field
        representation = super().to_representation(instance)

        created_at = instance.created_at
        if created_at:
            # Calculate the snippet's age in a human-readable format
            representation['title'] = Tag.objects.get(id=instance.tag_id).title
            representation['created_at'] = change_date_format(representation['created_at'])
            representation['updated_at'] = change_date_format(representation['updated_at'])
        return representation

    def get_detail_url(self, obj):
        return reverse('snippets', args=[obj.pk], request=self.context.get('request'))


class TagSerializer(serializers.ModelSerializer):
    """ Serializer for the Tag model. Used to validate and serialize tag data. """

    class Meta:
        model = Tag
        fields = ['id', 'title']


class SnippetSerializer(serializers.ModelSerializer):
    """ Serializer for the Snippet model. Used to validate and serialize snippet data along with related tag. """
    title = serializers.CharField()
    id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Snippet
        fields = ['note', 'title', 'id']
