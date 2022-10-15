from contextlib import nullcontext
from ctypes import addressof
import datetime
from email.policy import default
from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class user_ext(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    date_of_birth = models.DateField(default=datetime.date.today,null=True)
    image = models.ImageField(upload_to = 'user/pro_pic')
    gender = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    pincode = models.IntegerField()
    otp = models.ImageField()

class category(models.Model):
    name = models.CharField(max_length=255)
    image=models.ImageField(upload_to='category/image')
    
class product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product/image")
    category_id = models.ForeignKey(category,on_delete=models.CASCADE,null=True,blank=True)
    amount = models.IntegerField()

class productImage(models.Model):
    product_id =models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField()
    

class kart(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE,null=True,blank=True)


