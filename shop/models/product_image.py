from django.db import models


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='+')
    image = models.ImageField('product_images')
