import datetime

from django import forms
from .models import Material, Accessory, Product, Rest
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.forms import  Textarea, CharField



class AddModelProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('type','for_whom','name','used_materials','price_BYN','materials_price_BYN','photo','sell_date','to_whom_was_given','comment')
        labels = {
            'type': _('Type*:'),
            'for_whom': _('Was it to sell, as a gift, for me*:'),
            'to_whom_was_given': _('To whom it was given (Name: phone number), "Me" if empty:'),
            'price_BYN': _('Price BYN (0 if empty):'),
            'materials_price_BYN': _('Price of the used materials BYN (0 if empty):'),
            'sell_date': _('Date of selling (yyyy-MM-dd, today if empty):'),
        }
        widgets = {
            'used_materials': Textarea(attrs={'cols': 50, 'rows': 2}),
            'comment': Textarea(attrs={'cols': 50, 'rows': 2}),

        }


class AddModelMaterial(forms.ModelForm):

    class Meta:
        model = Material
        fields = ('type','article','manufacturer','trade_mark','series','color','effects','nominal_amount','real_amount','measure_units','unit_price_BYN','purchase_date','purchase_place','comment')
        labels = {
            'article': _('Article (for FIMO clay please add 4 numbers of series e.g. 8020, dash and color number)*'),
            'purchase_date': _('Date of purchase (yyyy-MM-dd,  today if empty):'),
            'type': _('Type*:'),
            'unit_price_BYN': _('Price of the unit BYN (0 if empty):'),
            'nominal_amount': _('Nominal amount (1 if empty):'),
            'real_amount': _('Real amount (Equals to Nominal if empty):'),
            'measure_units': _('Units of measure ("unit" if empty):'),
            'purchase_place': _('Where it was bought or found:'),
        }
        widgets = {
            'effects': Textarea(attrs={'cols': 55, 'rows': 2}),
            'comment': Textarea(attrs={'cols': 50, 'rows': 2}),
        }

    # def clean_manufacturer(self):
    #     trade_mark_data = self.cleaned_data['trade_mark']
    #     manufacturer_data = self.cleaned_data['manufacturer']
    #
    #     if trade_mark_data not in ['fimo','cernit'] and (manufacturer_data == None or manufacturer_data == ''):
    #         raise ValidationError("Please enter the manufacturer")
    #
    #     return manufacturer_data



class AddModelAccessory(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ('type','article','manufacturer','description','unit_price_BYN','purchase_date','purchase_place','comment')
        labels = {
            'type': _('Type*:'),
            'description': _('Description*:'),
            'purchase_date': _('Date of purchase (yyyy-MM-dd,  today if empty):'),
            'purchase_place': _('Where it was bought or found:'),
        }
        widgets = {
            'description': Textarea(attrs={'cols': 50, 'rows': 2}),
            'comment': Textarea(attrs={'cols': 50, 'rows': 2}),

        }

