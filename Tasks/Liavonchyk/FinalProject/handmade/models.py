from django.db import models

class Material(models.Model):
    type = models.CharField(max_length=100)
    article = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255, blank=True)
    trade_mark = models.CharField(max_length=100, blank=True)
    series = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    effects = models.TextField(blank=True)
    nominal_amount = models.FloatField(blank=True)
    real_amount = models.FloatField(blank=True)
    measure_units = models.CharField(max_length=100,blank=True)
    unit_price_BYN = models.FloatField(blank=True)
    unit_price_USD = models.FloatField()
    purchase_date = models.DateTimeField(blank=True)
    purchase_place = models.CharField(max_length=255,blank=True)
    update_timestamp = models.DateTimeField()
    comment = models.TextField(blank=True)

class Accessory(models.Model):
    type = models.CharField(max_length=100)
    article = models.CharField(max_length=255, blank=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    unit_price_BYN = models.FloatField(blank=True)
    unit_price_USD = models.FloatField()
    purchase_date = models.DateTimeField(blank=True)
    purchase_place = models.CharField(max_length=255,blank=True)
    update_timestamp = models.DateTimeField()
    comment = models.TextField(blank=True)


class Product(models.Model):
    FOR_WHOM_TYPES = [('s', 'sell'), ('g', 'gift'), ('m', 'myself')]

    type = models.CharField(max_length=100)
    for_whom = models.CharField(max_length=1, choices=FOR_WHOM_TYPES)
    name = models.CharField(max_length=255)
    used_materials = models.TextField(blank=True)
    price_BYN = models.FloatField(blank=True)
    price_USD = models.FloatField()
    materials_price_BYN = models.FloatField(blank=True)
    materials_price_USD = models.FloatField()
    photo = models.ImageField(upload_to='uploads',blank=True)
    sell_date = models.DateTimeField(blank=True)
    to_whom_was_given = models.CharField(max_length=255, blank=True)
    update_timestamp = models.DateTimeField()
    comment = models.TextField(blank=True)

class Rest(models.Model): #not used as of now
    type = models.CharField(max_length=100)
    article = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    trade_mark = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    color = models.CharField(max_length=100, blank=True)
    effects = models.TextField(blank=True)
    rest_amount = models.FloatField()
    measure_units = models.CharField(max_length=100)
    total_price_BYN = models.FloatField()
    total_price_USD = models.FloatField()
    update_timestamp = models.DateTimeField()
    comment = models.TextField(blank=True)
