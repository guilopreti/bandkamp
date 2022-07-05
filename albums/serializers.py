from rest_framework import serializers
from songs.serializers import SongSerializer

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ["id", "name", "musician_id", "total_duration", "songs"]
        read_only_fields = [
            "musician_id",
        ]

    total_duration = serializers.SerializerMethodField()

    def get_total_duration(self, album: Album):
        songs = album.songs.all()
        total_duration = 0
        for song in songs:
            total_duration += song.duration

        # outra forma:
        # from django.db.models import Sum
        # album.songs.aggregate(Sum('duration'))
        return total_duration

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
