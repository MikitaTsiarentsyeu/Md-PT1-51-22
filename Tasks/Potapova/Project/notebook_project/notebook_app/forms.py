from django import forms
from .models import Topic, Note
from django.core.exceptions import ValidationError


class TopicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self._owner = kwargs.pop('owner', None)
        super(TopicForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Topic
        fields = ['topic_name']

    def clean_topic_name(self):
        owner = self._owner
        topic_name_data = self.cleaned_data['topic_name']

        if Topic.objects.filter(owner_id=owner, topic_name=topic_name_data).count() > 0:
            raise ValidationError(f'Topic name {topic_name_data} already exists')
        return topic_name_data


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['topic'].queryset = Topic.objects.filter(owner_id=user)

    class Meta:
        model = Note
        fields = ['note_name', 'text', 'img', 'topic']
        labels = {'note_name': 'Note name', 'text': 'Note:', 'img': 'Image', 'topic': 'Topic list'}
        widgets = {'note_name': forms.TextInput(attrs={'cols': 80, 'rows': 1})}




