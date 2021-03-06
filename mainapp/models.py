from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images', blank=True)
    categories = models.ManyToManyField(ProductCategory)

    def __str__(self):
        return self.name
