from django.db import models

class Orders(models.Model):

    date = models.DateTimeField()
    name = models.CharField(max_length=36)
    phone = models.CharField(max_length=15)