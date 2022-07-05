import uuid

from django.db import models


# Create your models here.
class Song(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    duration = models.IntegerField(null=True)

    album = models.ForeignKey(
        "albums.Album", on_delete=models.CASCADE, related_name="songs"
    )
