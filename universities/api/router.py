from rest_framework.routers import DefaultRouter
from django.urls import path
from universities.api.views import UniversitiesApiViewSet, UniversitiesColorsApiViewSet

router_universities = DefaultRouter()
router_universities.register(prefix='', basename='universities', viewset=UniversitiesApiViewSet)


router_universities_colors = DefaultRouter()
router_universities_colors.register(prefix='', basename='universities_colors', viewset=UniversitiesColorsApiViewSet)