from rest_framework.routers import DefaultRouter
from django.urls import path
from ratings.api.views import RatingsApiViewSet

router_ratings = DefaultRouter()
router_ratings.register(prefix='', basename='ratings', viewset=RatingsApiViewSet)