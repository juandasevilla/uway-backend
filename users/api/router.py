from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.api.views import UserApiViewSet, users_are_activate, users_waiting_for_activate, roles_all, CustomTokenObtainPairView, get_info_user

router_user = DefaultRouter()
router_user.register(prefix='', basename='users', viewset=UserApiViewSet)

urlpatterns = [
    path('auth/login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me', get_info_user),
    path('user/are-activate-by-university/<id_university>', users_are_activate),
    path('user/waiting-for-activate-by-university/<id_university>', users_waiting_for_activate),
    path('role/', roles_all),

]