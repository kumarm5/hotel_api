from django.shortcuts import render
from .models import RestaurantDetails
from .serializers import RestaurantSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class RestaurantView(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated,)
    serializer_class = RestaurantSerializer
    queryset = RestaurantDetails.objects.all()
