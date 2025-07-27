from rest_framework.routers import DefaultRouter
from django.urls import path
from routes.api.views import RoutesApiViewSet, RouteUsersApiViewSet


router_routes = DefaultRouter()
router_routes.register(prefix='', basename='routes', viewset=RoutesApiViewSet)


router_route_users = DefaultRouter()
router_route_users.register(prefix='', basename='route_users', viewset=RouteUsersApiViewSet)