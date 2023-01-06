from django import forms 
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100, label="Title")
    subtitle = forms.CharField(max_length=200, label="Subtitle")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':"test-class"}), label='Content')
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)
    image = forms.ImageField(label="Image")

    def clean_subtitle(self):
        
        title_data = self.cleaned_data['title']
        subtitle_data = self.cleaned_data['subtitle']

        if title_data == subtitle_data:
            raise ValidationError("The title and subtitle shoul be different")
        
        return subtitle_data


class AddModelPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'post_type', 'image')
