from routes.api.serializer import RouteSerializer, RouteUserSerializer
from routes.models import Route, RouteUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


class RoutesApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RouteSerializer
    queryset = Route.objects.filter(deleted_at__isnull=True)


class RouteUsersApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RouteUserSerializer
    queryset = RouteUser.objects.filter(deleted_at__isnull=True)