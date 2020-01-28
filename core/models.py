# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.http import request
from django.urls import reverse

user = User.username


class Post(models.Model):
    title = models.TextField(max_length=250)
    posted_time = models.TimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=200, blank=True, null=True)
    comment = models.TextField(max_length=200, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})
