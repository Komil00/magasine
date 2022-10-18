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
    modelname = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    price = models.FloatField()
    productquantity = models.PositiveIntegerField()
    FOOT_CHOICES = (
        ("mans", "mans"),
        ("vomens", "womens"),
    )
    mode = models.CharField(max_length=9, choices=FOOT_CHOICES, default="mans")

    objects = models.Manager()

    def __str__(self):
        return self.modelname


class OrderProduct(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.modelname


class UserFavoriteProduct(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username
