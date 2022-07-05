from albums.models import Album
from albums.serializers import AlbumSerializer
from django.db.models import Sum
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from songs.models import Song
from songs.serializers import SongSerializer

from .models import Musician
from .serializers import MusicianSerializer


# Create your views here.
class MusicianView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    lookup_url_kwarg = "musician_id"


class MusicianAlbumView(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        # import ipdb

        # ipdb.set_trace()
        musician = get_object_or_404(Musician, pk=self.kwargs["musician_id"])

        greater_than = self.request.GET.get("duration_gt")
        lesser_than = self.request.GET.get("duration_lt")

        if greater_than:
            albums = Album.objects.filter(musician=musician)

            filtered_albums = []

            for album in albums:

                if not album.songs.count():
                    continue

                if album.songs.aggregate(Sum("duration"))["duration__sum"] > int(
                    greater_than
                ):
                    filtered_albums.append(album)

            return filtered_albums

        if lesser_than:
            albums = Album.objects.filter(musician=musician)

            filtered_albums = []

            for album in albums:

                if not album.songs.count():
                    filtered_albums.append(album)
                    continue

                if album.songs.aggregate(Sum("duration"))["duration__sum"] < int(
                    lesser_than
                ):
                    filtered_albums.append(album)

            return filtered_albums

        return Album.objects.filter(musician=musician)

    def perform_create(self, serializer):
        musician = get_object_or_404(Musician, pk=self.kwargs["musician_id"])

        serializer.save(musician=musician)


class MusicianAlbumSongView(generics.ListCreateAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        musician = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        album = get_object_or_404(Album, pk=self.kwargs["album_id"], musician=musician)

        return Song.objects.filter(album=album)

    def perform_create(self, serializer):

        musician = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        album = Album.objects.filter(
            musician=musician, id=self.kwargs["album_id"]
        ).first()

        if not album:
            raise Http404("Album not Found")

        serializer.save(album=album)


# class MusicianAlbumSongView(APIView):
#     def get(self, request, musician_id, album_id):
#         musician = get_object_by_id(Musician, musician_id)
#         album = get_object_by_id(Album, album_id)
#         songs = Song.objects.filter(album=album)

#         serializer = SongSerializer(songs, many=True)

#         return Response(serializer.data)

#     def post(self, request, musician_id, album_id):
#         musician = get_object_by_id(Musician, musician_id)

#         album = Album.objects.filter(musician=musician, id=album_id).first()

#         if not album:
#             return Response({"detail": "Album not Found"}, status.HTTP_404_NOT_FOUND)

#         serializer = SongSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(album=album)

#         return Response(serializer.data, status.HTTP_201_CREATED)
