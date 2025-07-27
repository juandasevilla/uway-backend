from universities.api.serializer import UniversitySerializer, UniversityColorsSerializer
from universities.models import University, UniversityColors
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


class UniversitiesApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UniversitySerializer
    queryset = University.objects.filter(deleted_at__isnull=True)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def universities_waiting_for_activate(request):
    universities = University.objects.filter(is_active=False, deleted_at__isnull=True)
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def universities_are_activate(request):
    universities = University.objects.filter(is_active=True, deleted_at__isnull=True)
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class UniversitiesColorsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UniversityColorsSerializer
    queryset = UniversityColors.objects.filter(deleted_at__isnull=True)