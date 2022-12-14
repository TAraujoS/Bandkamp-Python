from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics
from django.shortcuts import get_object_or_404
import ipdb
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    post=extend_schema(
        description="Route for Creating Songs",
        summary="Create Songs",
        tags=["Songs"],
    ),
    get=extend_schema(
        description="Route for Reading Songs",
        summary="Read Songs",
        tags=["Songs"],
    ),
)
class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs["pk"])
        return serializer.save(album=album)
