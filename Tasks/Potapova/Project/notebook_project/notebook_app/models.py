from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about."""
    topic_name = models.CharField(max_length=50, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ('topic_name', 'owner')

    def __str__(self):
        """Return a string representation of the model."""
        return self.topic_name


class Note(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    note_name = models.TextField(null=False)
    text = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='note_images/', null=True, blank=True, verbose_name='Image')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('note_name', 'topic')

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text


# Not implemented
class MultipleImage(models.Model):
    images = models.FileField()

