from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm
import datetime


class Template(models.Model):
    name = models.CharField(max_length=128)
    description=models.TextField(default=" ")
    groups = models.ManyToManyField(Group, through='TemplateGroup')
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
    current_group=models.ForeignKey(Group, null=True)
    level=models.IntegerField(default=0)
    status=models.CharField(max_length=32)

    def __str__(self):
        return self.user_name


class TemplateGroup(models.Model):
    template = models.ForeignKey(Template)
    group = models.ForeignKey(Group)
    number = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('number',)
