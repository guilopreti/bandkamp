from django.urls import path

from . import views

urlpatterns = [
    path("musicians/", views.MusicianView.as_view()),
    path("musicians/<uuid:musician_id>/", views.MusicianDetailView.as_view()),
    path("musicians/<uuid:musician_id>/albums/", views.MusicianAlbumView.as_view()),
    path(
        "musicians/<uuid:musician_id>/albums/<uuid:album_id>/songs/",
        views.MusicianAlbumSongView.as_view(),
    ),
]
