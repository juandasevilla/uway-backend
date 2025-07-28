from rest_framework.routers import DefaultRouter
from django.urls import path
from universities.api.views import UniversitiesApiViewSet, UniversitiesColorsApiViewSet, universities_are_activate, \
    universities_waiting_for_activate, universities_to_super_admin, activate_university


router_universities = DefaultRouter()
router_universities.register(prefix='', basename='universities', viewset=UniversitiesApiViewSet)


router_universities_colors = DefaultRouter()
router_universities_colors.register(prefix='', basename='universities_colors', viewset=UniversitiesColorsApiViewSet)


urlpatterns = [
    path('universities/waiting_for_activate/', universities_waiting_for_activate),
    path('universities/are_activate/', universities_are_activate),
    path('universities/to_super_admin/', universities_to_super_admin),
    path('universities/activate/<id_university>/', activate_university),
]
