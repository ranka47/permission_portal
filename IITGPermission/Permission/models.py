from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm

import datetime

class Task(models.Model):
    """
    Task (Permission) database
    """
    user_name = models.CharField(max_length=100)
    user_department = models.CharField(max_length=100)
    user_designation = models.CharField(max_length=100)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    purpose = models.TextField()
    facilities_required = models.TextField()
	
    def __str__(self):
        return self.user_name

