from django.contrib import admin
from .models import CreditRequest, Review, Consultation

admin.site.register( CreditRequest)
admin.site.register(Review)
admin.site.register(Consultation)