from rest_framework.routers import DefaultRouter
from django.urls import path
from routes.api.views import RoutesApiViewSet, RouteUsersApiViewSet, routes_by_user, available_routes_for_user_by_university


router_routes = DefaultRouter()
router_routes.register(prefix='', basename='routes', viewset=RoutesApiViewSet)


router_route_users = DefaultRouter()
router_route_users.register(prefix='', basename='route_users', viewset=RouteUsersApiViewSet)


urlpatterns = [
    path('routes/by-user/<id_user>', routes_by_user),
    path('routes/available-by-university/<id_university>', available_routes_for_user_by_university),
]
