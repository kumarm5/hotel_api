from django.urls import path, re_path, include
from rest_framework import routers
from restaurant import views

router = routers.DefaultRouter()
router.register(r'restaurant', views.RestaurantView)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
