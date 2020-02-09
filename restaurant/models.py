from django.db import models


# Create your models here.
class RestaurantDetails(models.Model):
    restaurant_name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.restaurant_name

    class Meta:
        verbose_name = "Restaurant Detail"
        verbose_name_plural = "Restaurant Details"
