# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    text=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User)

    def __unicode__(self):
        return self.text

class Note(models.Model):

    
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.text[:50]
