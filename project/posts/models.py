# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField()
    body  = models.TextField()
    date  = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None)

    def __str__(self):
        return self.title


    def snippet(self):
        if len(self.body) > 300:
            return self.body[:300] + " ..."
        return self.body