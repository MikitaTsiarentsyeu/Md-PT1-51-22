from .models import RealtorForm
from django.forms import ModelForm, TextInput, Textarea


class RealtorFormCall(ModelForm):
    class Meta:
        model = RealtorForm
        fields =["user_name", "user_phone", "user_mail"]
        widgets = {
            "user_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "user_phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "user_mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш e-mail'
            }),
        }


class RealtorFormMail(ModelForm):
    class Meta:
        model = RealtorForm
        fields =["user_name", "user_mail", "user_comment"]
        widgets = {
            "user_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "user_mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш e-mail'
            }),
            "user_comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш вопрос'
            }),
        }