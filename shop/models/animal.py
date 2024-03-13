from django.db import models


class Animal(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='animal_covers')

    def __str__(self):
        return self.title

    def get_products(self):
        from shop.models import Product
        return Product.objects.filter(animal=self)
