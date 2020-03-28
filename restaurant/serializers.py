from rest_framework import serializers
from .models import (
    RestaurantDetails,
    Product
)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantDetails
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
