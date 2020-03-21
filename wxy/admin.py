# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from wxy.models import Subject ,Note

# Register your models here.
admin.site.register(Subject)
admin.site.register(Note)
