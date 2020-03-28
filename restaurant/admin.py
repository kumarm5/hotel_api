from django.contrib import admin
from .models import (
    RestaurantDetails,
    Product
)

# Register your models here.


class RestaurantDetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(RestaurantDetails, RestaurantDetailsAdmin)


admin.site.register(Product)

