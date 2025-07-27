from rest_framework.views import APIView
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.api.serializers import LoginSerializer, RegisterSerializer, RoleSerializer
from datetime import datetime
from roles.models import Role

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(email=request.data['email'])
        user_data = LoginSerializer(user).data

        response.data.update({'user': user_data})
        return response

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in 'create':
            self.permission_classes = [AllowAny,]
        return super(self.__class__, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'id': serializer.data['id'],
                'username': serializer.data['username'],
                'email': serializer.data['email'],
            }
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        serializer = LoginSerializer(
            User.objects.filter(deleted_at=None), many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        try:
            if serializer.validated_data['password'] is not None:
                instance.set_password(serializer.validated_data['password'])
                instance.save()
        except KeyError:
            pass
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.deleted_at = datetime.now()
        user.save()
        serializer = LoginSerializer(user)
        data = {
            'status': 'ok',

        }
        return Response(data=data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_waiting_for_activate(request, id_university):
    users = User.objects.filter(is_active=False, deleted_at__isnull=True, university_id=id_university)
    serializer = LoginSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_are_activate(request, id_university):
    users = User.objects.filter(is_active=True, deleted_at__isnull=True, university_id=id_university)
    serializer = LoginSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def roles_all(request):
    roles = Role.objects.all()
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_info_user(request):
    user = request.user
    serializer = LoginSerializer(user)
    response_data = serializer.data

    return Response(response_data)