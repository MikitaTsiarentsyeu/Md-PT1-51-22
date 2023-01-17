from django import forms
from .models import MyModel

from django.forms import ModelForm



class AddModelPost(forms.ModelForm):

    class Meta:
        model = MyModel
        fields = ('name', 'name_of_kid', 'class_choice', 'phone', 'comment')

