from musicians.models import Musician
from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "name", "duration", "album_id", "musician_id"]
        read_only_fields = ["album_id"]

    musician_id = serializers.SerializerMethodField()

    def get_musician_id(self, song: Song):
        return song.album.musician.id

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
