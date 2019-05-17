# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Products(models.Model):
      # banner = models.ImageField(upload_to='media/',blank=True,null=True)
      name= models.CharField(max_length=254,blank=True,null=True)
      main_category =models.ImageField(upload_to='media',null=True,blank=True)
      price=models.FloatField(null=True,blank=True)


class SubProducts(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to='media/',blank=True,null=True)
    name = models.CharField(max_length=254,null=True,blank=True)
    old_price = models.FloatField(null=True, blank=True)
    new_price = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    measure = models.CharField(max_length=254, null=True, blank=True)
    tax=models.FloatField(null=True,blank=True)
    discount=models.FloatField(null=True,blank=True)
    description=models.CharField(max_length=254,null=True,blank=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=254,null=True,blank=True)
    slug = models.CharField(max_length=254,null=True,blank=True)
    is_active = models.BooleanField(default=True)



