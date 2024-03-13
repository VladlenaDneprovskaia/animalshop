from datetime import timedelta

from django.db import models
from django.db.models import QuerySet
from django.utils import timezone

from .animal import Animal
from .brand import Brand
from .product_image import ProductImage


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_new_price(self):
        return self.price - self.discount

    def get_old_price(self):
        return self.price

    def has_discount(self):
        return self.discount != 0

    def get_discount_percent(self):
        return (self.discount / self.price) * 100

    def is_new(self):
        return timezone.now() - timedelta(days=30) < self.created

    def images(self):
        return [images.image for images in ProductImage.objects.filter(product=self).all()]
