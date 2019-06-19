from django.db import models
import datetime


class Tag(models.Model):
    name = models.CharField(max_length=32) # if you want unique names add unique=True and migrate db changes
    create_date = models.DateField(default=datetime.date.today)


class Task(models.Model):
    name = models.CharField(max_length=64) # if you want unique names add unique=True and migrate db changes
    descr = models.TextField()
    tag = models.ManyToManyField('Tag', related_name='tasks', blank=True)
    create_date = models.DateField(default=datetime.date.today)