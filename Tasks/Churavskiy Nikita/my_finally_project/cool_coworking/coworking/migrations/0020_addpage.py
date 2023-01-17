# Generated by Django 4.1.3 on 2022-12-23 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0019_delete_newpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название Коворкинга')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('num', models.CharField(max_length=255, null=True, verbose_name='Номер улицы')),
                ('number', models.CharField(max_length=255, verbose_name='Контактный номер')),
                ('content', models.TextField(blank=True, unique=True, verbose_name='Описание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coworking.cities', verbose_name='Города')),
            ],
            options={
                'verbose_name': 'Статьи пользователя',
                'verbose_name_plural': 'Статьи пользователя',
                'ordering': ['time_update'],
            },
        ),
    ]
