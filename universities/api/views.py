from universities.api.serializer import UniversitySerializer, UniversityColorsSerializer
from universities.models import University, UniversityColors
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from users.api.serializers import RegisterSerializer
from users.models import User


class UniversitiesApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UniversitySerializer
    queryset = University.objects.filter(deleted_at__isnull=True)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            university = serializer.save()
            user_data = {
                "email": request.data.get("email"),
                "username": request.data.get("email"),
                "identification_document": request.data.get("identification_document"),
                "phone_number": request.data.get("phone_number"),
                "password": request.data.get("password"),
                "address": university.address,
                "university": university.id,
                "is_staff": True,
                "is_active": False
            }
            user_serializer = RegisterSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({
                    "university": serializer.data,
                }, status=status.HTTP_201_CREATED)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def universities_waiting_for_activate(request):
    universities = University.objects.filter(is_active=False, deleted_at__isnull=True)
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def universities_are_activate(request):
    universities = University.objects.filter(is_active=True, deleted_at__isnull=True)
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def universities_to_super_admin(request):
    universities = University.objects.filter(deleted_at__isnull=True)
    serializer = UniversitySerializer(universities, many=True)
    data = []
    for uni, uni_data in zip(universities, serializer.data):
        user = User.objects.filter(university=uni, is_staff=True).first()
        uni_data['staff_email'] = user.email if user else None
        data.append(uni_data)
    return Response(data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def activate_university(request, id_university):
    try:
        university = University.objects.get(id=id_university, deleted_at__isnull=True)
        university.is_active = True
        university.save()
        serializer = UniversitySerializer(university)
        user = User.objects.filter(university=university, is_staff=True).first()
        if user:
            user.is_active = True
            user.save()
        else:
            return Response({"error": "Staff user not found for this university"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except University.DoesNotExist:
        return Response({"error": "University not found"}, status=status.HTTP_404_NOT_FOUND)


class UniversitiesColorsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UniversityColorsSerializer
    queryset = UniversityColors.objects.filter(deleted_at__isnull=True)