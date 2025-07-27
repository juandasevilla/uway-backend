from ratings.api.serializer import RatingSerializer
from ratings.models import Rating
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


class RatingsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RatingSerializer
    queryset = Rating.objects.filter(deleted_at__isnull=True)