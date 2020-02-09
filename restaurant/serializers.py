from rest_framework import serializers
from .models import RestaurantDetails


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantDetails
        fields = '__all__'
