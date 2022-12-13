from rest_framework import serializers
from albums.serializers import AlbumSerializer
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Song
        fields = "__all__"
        read_only_fields = ["album"]
