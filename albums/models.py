import uuid

from django.db import models


class Album(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)

    musician = models.ForeignKey(
        "musicians.Musician", on_delete=models.CASCADE, related_name="albums"
    )
