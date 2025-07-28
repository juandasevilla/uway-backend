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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def routes_by_user(request, id_user):
    routes = Route.objects.filter(driver_id=id_user, deleted_at__isnull=True)
    serializer = RouteSerializer(routes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def available_routes_for_user_by_university(request, id_university):
    routes = Route.objects.filter(
        driver__university_id=id_university,
        deleted_at__isnull=True
    )
    data = []
    for route in routes:
        driver = route.driver
        route_data = RouteSerializer(route).data
        route_data['driver_identification_document'] = driver.identification_document
        route_data['driver_full_name'] = f"{driver.first_name} {driver.last_name}"
        data.append(route_data)
    return Response(data, status=status.HTTP_200_OK)


class RouteUsersApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RouteUserSerializer
    queryset = RouteUser.objects.filter(deleted_at__isnull=True)