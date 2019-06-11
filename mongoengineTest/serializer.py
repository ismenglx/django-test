from rest_framework_mongoengine import serializers as s1

from mongoengineTest.models import Author


class AuthorSerializer(s1.DocumentSerializer):
    class Meta:
        model = Author
        fields = ('_id', 'name', 'h_index', 'pubs')
