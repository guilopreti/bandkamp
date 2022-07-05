import albums
from albums.serializers import AlbumSerializer
from rest_framework import serializers

from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Musician
        fields = ["id", "first_name", "last_name", "instrument", "albums"]

    def create(self, validated_data):
        return Musician.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
