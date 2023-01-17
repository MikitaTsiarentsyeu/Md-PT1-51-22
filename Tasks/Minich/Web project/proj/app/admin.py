from django.contrib import admin
from .models import Client,Statement,InsuranceNumber

admin.site.register(Client)
admin.site.register(Statement)
admin.site.register(InsuranceNumber)
# Register your models here.
