from vehicles.api.serializer import VehicleSerializer
from vehicles.models import Vehicle
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


class VehiclesApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.filter(deleted_at__isnull=True)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vehicle_by_user(request, id_user):
    vehicles = Vehicle.objects.filter(driver=id_user, deleted_at__isnull=True)
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)