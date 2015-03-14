from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm
import datetime


class Template(models.Model):
    name = models.CharField(max_length=128)
    description=models.TextField(default=" ")
    users = models.ManyToManyField(User, through='TemplateUser')
    def __str__(self):
        return self.name

class Task(models.Model):
    """
    Task (Permission) database
    """
    template_id=models.ForeignKey(Template)
    user_name = models.CharField(max_length=100)
    # user_department = models.CharField(max_length=100)
    # user_designation = models.CharField(max_length=100)

    from_date = models.DateField()
    from_time=models.TimeField()
    to_date = models.DateField()
    to_time = models.TimeField()

    purpose = models.TextField()
    facilities_required = models.TextField()
    current_user=models.ForeignKey(User, null=True)
    level=models.IntegerField(default=1)
    status=models.CharField(max_length=32, default="Pending")
    approved_or_denied_by=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.user_name


class TemplateUser(models.Model):
    template = models.ForeignKey(Template)
    user = models.ForeignKey(User)
    number = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('number',)

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)
    text = models.TextField()
    task = models.ForeignKey(Task)
