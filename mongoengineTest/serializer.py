from rest_framework_mongoengine import serializers

from mongoengineTest.models import Author


class AuthorSerializer(serializers.DynamicDocumentSerializer):
    class Meta:
        model = Author
        fields = ('_id', 'name', 'h_index', 'pubs')
