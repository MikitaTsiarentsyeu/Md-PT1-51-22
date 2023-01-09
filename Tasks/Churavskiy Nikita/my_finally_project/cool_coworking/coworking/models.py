from django.urls import reverse
from django.db import models


class coworking(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank = True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время добавления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коворкинги'
        verbose_name_plural = 'Коворкинги'
        ordering = ['title', 'time_update']


class location(models.Model):
    street = models.CharField(max_length=255, verbose_name='Улица')
    num = models.CharField(max_length=255, verbose_name='Номер улицы')
    number = models.CharField(max_length=255, verbose_name='Контактный номер')
    content = models.TextField(blank=True, verbose_name='Содержание')
    cat = models.ForeignKey('cities', on_delete=models.PROTECT, null=True, verbose_name='Города')
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.street

    class Meta:
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположение'
        ordering = ['time_update']
        

class cities(models.Model):
    title = models.CharField(max_length=255, verbose_name='Город')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank = True, verbose_name='Фото')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null = True)
    content = models.TextField(blank=True, verbose_name='Содержание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Города Беларуси'
        verbose_name_plural = 'Города Беларуси'



class Addpage(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название Коворкинга')
    street = models.CharField(max_length=255, verbose_name='Улица')
    num = models.CharField(max_length=255, verbose_name='Контактный номер', null=True)
    email = models.EmailField(max_length=255, verbose_name='Email', null=True)
    content = models.TextField(blank=True,unique=True, verbose_name='Описание')
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    cat = models.ForeignKey('cities', on_delete=models.PROTECT, null=True, verbose_name='Города')


    def __str__(self):
        return self.street


    def get_absolute_url(self):
        return reverse('ua_page')


    class Meta:
        verbose_name = 'Статьи пользователя'
        verbose_name_plural = 'Статьи пользователя'
        ordering = ['time_update']
    


class AboutBelarus(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    content = models.TextField(blank=True,unique=True, verbose_name='Контент')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank = True, verbose_name='Фото')
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
   

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'О Беларуси'
        verbose_name_plural = 'О Беларуси'
        ordering = ['time_update']




