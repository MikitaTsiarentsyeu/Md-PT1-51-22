from django import forms
from .models import Statement, InsuranceNumber
from django.core.exceptions import ValidationError

class AddModelStatement(forms.ModelForm):

    class Meta:
        model = Statement
        fields = ('insurance_num','brand','model','year_auto','photo_damage')

        def test(self):
            model_data = self.cleaned_data['model']
            ValidationError("Insurance number not found")        
        
   
class AddStatementManual(forms.Form):
    brand = forms.CharField(max_length=50, label="Brand")
    model = forms.CharField(max_length=50, label="Model")
    photo_damage = forms.ImageField(label="Photo damage")

        

   