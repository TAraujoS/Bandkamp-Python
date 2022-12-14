from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    post=extend_schema(
        description="Route for Creating Users",
        summary="Create Users",
        tags=["Users"],
    )
)
class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


@extend_schema_view(
    get=extend_schema(
        description="Route for Reading Users",
        summary="Read Users",
        tags=["Users"],
    ),
    patch=extend_schema(
        description="Route for Updating Users",
        summary="Update Users",
        tags=["Users"],
    ),
    delete=extend_schema(
        description="Route for Deleting Users",
        summary="Delete Users",
        tags=["Users"],
    ),
)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
