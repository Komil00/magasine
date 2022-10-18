from customuser.models import CustomUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    modelname = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    productquantity = models.PositiveIntegerField()
    FOOT_CHOICES = (
        ("mans", "mans"),
        ("vomens", "womens"),
    )
    mode = models.CharField(max_length=9, choices=FOOT_CHOICES, default="mans")

    def __str__(self):
        return self.modelname


class UserFavoriteProduct(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username


class OrderProduct(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.modelname
