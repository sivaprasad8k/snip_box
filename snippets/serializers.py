from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Snippet
from .models import Tag


class SnippetDetailSerializer(serializers.ModelSerializer):
    """Serializer class for the Snippet model."""
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Snippet
        fields = ['note', 'detail_url']

    def to_representation(self, instance):
        """Add Tite to the response"""
        representation = super().to_representation(instance)
        representation['title'] = Tag.objects.get(id=instance.tag_id).title
        return representation

    def get_detail_url(self, obj):
        """Add Url to get the details of each snippet object"""
        return reverse('snippets', args=[obj.pk], request=self.context.get('request'))


class SnippetSerializer(serializers.ModelSerializer):
    """ Serializer for the Snippet model. Used to validate and serialize snippet data along with related tag. """
    title = serializers.CharField()
    id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Snippet
        fields = ['note', 'title', 'id']
