# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from register.models import Signup,Document

admin.site.register(Signup)

admin.site.register(Document)