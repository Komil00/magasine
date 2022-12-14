from django.dispatch import receiver
from django.template.defaultfilters import slugify

from customuser.models import CustomUser
from django.db import models
from django.db.models.signals import pre_save, post_save


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    modelname = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    productquantity = models.IntegerField()
    FOOT_CHOICES = (
        ("mans", "mans"),
        ("vomens", "womens"),
    )
    mode = models.CharField(max_length=9, choices=FOOT_CHOICES, default="mans")

    objects = models.Manager()

    def __str__(self):
        return self.modelname


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='image')


# @receiver(pre_save, sender=Product)
# def product_pre_save(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.modelname)


# @receiver(post_save, sender=Product)
# def product_post_save(sender, instance, created, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.modelname)
#         instance.save()


class OrderProduct(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.modelname


# @receiver(post_save, sender=OrderProduct)
# def create_order(instance, created, *args, **kwargs):
#     if created:
#         product = instance.product
#         product.productquantity -= instance.quantity
#         product.save()


class UserFavoriteProduct(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username
