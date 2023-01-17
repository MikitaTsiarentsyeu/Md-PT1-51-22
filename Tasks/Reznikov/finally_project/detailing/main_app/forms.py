from django import forms
from django.core.exceptions import ValidationError
from .models import Orders

class PopupForm(forms.Form):

    date = forms.DateTimeField()
    name = forms.CharField(max_length=36, min_length=3, label='Name')
    phone = forms.CharField(max_length=15, min_length=5, label='Phone', help_text="Укажите в формате +375291234567")

    def clean_date(self):
        date = self.cleaned_data['date']
        
        string_date = str(date)
        
        if len(string_date) != 19:
            raise ValidationError("Выберите дату и время записи")

        if string_date[10] != ' ' and string_date[13] != ':':
            raise ValidationError("Выберите дату и время записи")

        if string_date.split(' ')[1].split(':')[0] == '00':
            raise ValidationError("Выберите время записи")
        
        check_free_time = Orders.objects.filter(date__contains=date).values()
        
        if check_free_time:
            raise ValidationError("Выбранное время уже занято")
            
        return date

    def clean_name(self):
        
        name = self.cleaned_data['name']

        if name.isalpha() == False:
            raise ValidationError("В имени можно использовать только буквы")
        if len(name) < 3 or len(name) > 36:
            raise ValidationError("Длина имени не может быть меньше 3 или больше 36")
        
        return name
    
    def clean_phone(self):
        
        phone = self.cleaned_data['phone']
        
        if phone[0] != '+':
            raise ValidationError("Номер должен начинаться со знака \"+\"")
        
        for index, num in enumerate(phone):
            if num.isdigit() == False and index != 0:
                raise ValidationError("В номере можно использовать только цифры")
    
        if len(phone) < 5 or len(phone) > 15:
            raise ValidationError("Номер не может быть меньше 5 или больше 15")
        
        return phone
  