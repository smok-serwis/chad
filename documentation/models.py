import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Project label')
    slug = models.CharField(max_length=255, verbose_name='Project slug', unique=True)
    created_on = models.DateTimeField(default=datetime.datetime.now, verbose_name='Created on')
    website = models.TextField(null=True, verbose_name='URL to the website')
    description = models.TextField(verbose_name='Project description')


class Item(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(default=datetime.datetime.now)
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    importance = models.IntegerField(default=10)    # 1 is most important, 20 is least important


class Entry(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    mimetype = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    data = models.BinaryField()
