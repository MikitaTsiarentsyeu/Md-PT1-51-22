from django.db import models
from django.core.validators import RegexValidator





class MyModel(models.Model):

    CLSS_TYPES = [('U', ' Unity game development class'), ('W', ' Web development class'), ('P', ' Python programming class') ]

    name = models.CharField(max_length=100)
    name_of_kid = models.CharField(max_length=100)
    
    issued = models.DateTimeField()
    class_choice = models.CharField(max_length=1, choices=(CLSS_TYPES), default='U')
    phone = models.CharField( max_length=16,blank=False,null=True,validators=[RegexValidator(regex=r'^\+\d{9,15}$',message="Phone must be entered in format '+123456789'")])
    comment = models.TextField(blank=True)

    


