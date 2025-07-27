from rest_framework.routers import DefaultRouter
from django.urls import path
from vehicles.api.views import VehiclesApiViewSet, vehicle_by_user

router_vehicles = DefaultRouter()
router_vehicles.register(prefix='', basename='vehicles', viewset=VehiclesApiViewSet)

urlpatterns = [
    path('vehicles/by-user/<id_user>', vehicle_by_user),
]