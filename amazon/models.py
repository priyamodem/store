from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=30,null=True)
    description=models.TextField()


class Product(models.Model):
    name=models.CharField(max_length=30,null=True)
    serialnumber=models.CharField(max_length=35,unique=True)
    price=models.FloatField()
    description=models.CharField(max_length=40,null=True)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=None)

class ProductImage(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
     image=models.ImageField(upload_to='product_image/')

class UserDetails(models.Model):
      mobile=models.CharField(max_length=15,null=True)
      address=models.TextField()
      user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)


class Cart(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)


# Create your models here.
