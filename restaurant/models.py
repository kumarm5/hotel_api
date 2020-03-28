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


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    restaurant = models.ForeignKey(RestaurantDetails, related_name="restaurant_product", on_delete=models.CASCADE)
    product_image = models.ImageField(blank=True, verbose_name='product_image')
    price = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
