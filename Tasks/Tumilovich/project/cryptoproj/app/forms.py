from django import forms
from .models import Sub, Comments


class AddSubForm(forms.ModelForm):

    class Meta:
        model = Sub
        fields = ('name', 'sub_type', 'email')



class AddComForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('name', 'comment')



# class AddComForm(forms.Form):
#
#     name = forms.CharField(max_length=30, label='Name')
#     comment = forms.CharField(max_length=100)