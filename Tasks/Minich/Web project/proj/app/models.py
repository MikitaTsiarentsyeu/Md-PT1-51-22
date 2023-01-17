from django.db import models
from django import forms

class Client(models.Model):
    firstname = models.CharField(max_length=50)
    lasttname = models.CharField(max_length=50)
    email = models.EmailField() 

choices_status = (
        ('New', 'New'),
        ('Work', 'In work'),
        ('Agreement', 'Agreement'),
        ('Finish', 'Finish'),
    )

class Statement(models.Model):

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    photo_damage = models.ImageField(upload_to='uploads')
    client = models.ForeignKey('Client',on_delete=models.CASCADE)   
    date_st = models.DateTimeField()
    year_auto = models.CharField(max_length=4)
    insurance_num = models.CharField(max_length=20)
    status_st = models.CharField(max_length=300, choices = choices_status)

class InsuranceNumber(models.Model):
    number = models.CharField(max_length=30)
    email = models.EmailField()
