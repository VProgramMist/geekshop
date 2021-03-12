from django.db import models
from authapp.models import User
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина для {self.user.username} | Продукт {self.product.name}"

    @property
    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        return sum([elem.quantity * elem.product.price for elem in
                    Basket.objects.filter(user=self.user)]) if Basket.objects.filter(user=self.user) else 0

    def total_count(self):
        return sum([elem.quantity for elem in Basket.objects.filter(user=self.user)]) if Basket.objects.filter(
            user=self.user) else 0
