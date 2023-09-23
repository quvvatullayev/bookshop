from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class AuthUser(User):
    # name = models.CharField(max_length=30)
    tg_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField(default=1)

    def __str__(self) -> str:
        return str(AuthUser.name[:10]+'|'+Product.book_name[:10])

class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(AuthUser.name[:10]+'|'+Product.book_name[:10])