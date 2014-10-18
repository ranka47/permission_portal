from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm

import datetime



class Template(models.Model):
    name = models.CharField(max_length=128)
    description=models.TextField(default=" ")
    hierarchy_1=models.CharField(blank=True, max_length=32)
    hierarchy_2=models.CharField(blank=True, max_length=32)
    hierarchy_3=models.CharField(blank=True, max_length=32)
    hierarchy_4=models.CharField(blank=True, max_length=32)
    hierarchy_5=models.CharField(blank=True, max_length=32)
    def __str__(self):
        return self.name
class Task(models.Model):
    """
    Task (Permission) database
    """
    
    template_id=models.ForeignKey(Template)
    user_name = models.CharField(max_length=100)
    user_department = models.CharField(max_length=100)
    user_designation = models.CharField(max_length=100)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    purpose = models.TextField()
    facilities_required = models.TextField()
    current_group=models.ForeignKey(Group)

    def __str__(self):
        return self.user_name
