from BookmarkApi.models import Bookmark
from rest_framework import serializers


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'phrase')