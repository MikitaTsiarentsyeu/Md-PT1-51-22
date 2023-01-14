from django import forms
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

class AddPostForm(forms.ModelForm):

    def __init__ (self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

        
    class Meta:
        model = Addpage
        fields = ['title','street', 'num', 'email', 'content', 'cat']


        widgets = {
        'title': forms.Textarea(attrs={'cols': 25, 'rows': 1}),
        'street': forms.Textarea(attrs={'cols': 25, 'rows': 1}),
        'num': forms.Textarea(attrs={'cols': 25, 'rows': 1}),
        'number': forms.Textarea(attrs={'cols': 25, 'rows': 1}),
        'content': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        fields = ['username','password1','password2']
