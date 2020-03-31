from django.shortcuts import render
from .models import (
    RestaurantDetails,
    Product
)
from .serializers import (
    RestaurantSerializer,
    ProductSerializer
)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class RestaurantView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantSerializer
    queryset = RestaurantDetails.objects.all()


class ProductView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
