from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm

class Task(models.Model):
    permission_type=models.CharField(max_length=32)
    applicant=models.CharField(max_length=32)
    date_of_application=models.DateTimeField(auto_now_add=True)
    subject=models.CharField(max_length=128, blank=False)
    description=models.TextField(blank=False)
    special_mentions=models.TextField(blank=True)
    required_files=models.FileField(upload_to='files', null=True, blank=True)
    urgency=models.DateField(null=True, blank=True)
    status=models.TextField()
    status_description=models.TextField()
    # pass_it_to=models.CharField(max_length=32)

    def __str__(self):
        return str(self.applicant+" "+self.subject)

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)
    text = models.TextField()
    task = models.ForeignKey(Task)