from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import datetime



class Template(models.Model):
    name = models.CharField(max_length=128)
    description=models.TextField(default=" ")
    hierarchies = models.ManyToManyField(Group,  related_name='groups')
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
