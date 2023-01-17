from django.db import models
import datetime

class Sub(models.Model):

    SUB_TYPES = [('0', 'new to crypto'), ('1', 'already in crypto')]

    name = models.CharField(blank=False, max_length=100)
    sub_type = models.CharField(max_length=1, choices=SUB_TYPES)
    email = models.EmailField(blank=False, primary_key=True)


class Comments(models.Model):
    name = models.CharField(max_length=30)
    comment = models.TextField(max_length=200)
    issued = models.DateTimeField()