# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Products, SubProducts, Manufacturer

# Register your models here.

admin.site.register(Products)
admin.site.register(SubProducts)
admin.site.register(Manufacturer)