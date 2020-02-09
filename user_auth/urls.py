from django.urls import path, re_path, include
from rest_framework_simplejwt import views as jwt_views
from .views import (
    RegisterView,
    ChangePasswordView,
    UserProfileView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', UserProfileView)

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    re_path(r'^', include(router.urls)),
]

