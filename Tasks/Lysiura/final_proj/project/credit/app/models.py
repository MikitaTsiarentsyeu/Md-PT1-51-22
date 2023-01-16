from django.db import models

    
class CreditRequest(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    birthday = models.DateField()
    passport_id  = models.CharField(max_length=9)
    card_number = models.IntegerField()
    number = models.CharField(max_length=12)
    sum_of_cred = models.IntegerField()
    period = models.IntegerField()
    
class Review(models.Model):
    date = models.DateTimeField()
    question = models.CharField(max_length=1000)
    
class Consultation(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    ask = models.CharField(max_length=1000)