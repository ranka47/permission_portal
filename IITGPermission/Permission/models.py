from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm

import datetime
# Create your models here.

class Permission(models.Model):
	name=models.CharField(max_length=128)
	display_name=models.CharField(max_length=255)
	description=models.TextField()

	# def __init__(self,name,display_name,description):
	# 	self.name=name
	# 	self.display_name=display_name
	# 	self.description=description


class Template(models.Model):
	#permission_id=models.ForeignKey(Permission)
	name=models.CharField(max_length=255)
	description=models.TextField()
	def __str__(self):
		return self.name

class TaskUser(models.Model):
	def userfunction(request):
		user_id=request.user.username
	
	template_id=models.ForeignKey(Template)
	name=models.CharField(max_length=255)
	
	description=models.TextField()
	created_at=models.DateField(auto_now_add=True)
	updated_at=models.DateField(auto_now=True)
	description1=models.TextField()
	group_id=models.ForeignKey(Group)
	#TaskGroup_id.Approval()
	#approved=models.BooleanField(default=False)
	def __str__(self):
		return self.name

class TaskGroup(models.Model):
	task_id=models.ForeignKey(TaskUser)
	approved=models.BooleanField(default=False)
	def Approval(self):
	 	if self.approved==True:
	 		self.task_id.description1='Approved'
	#def __str__(self):
	#	return self.task_id.name

class Task(models.Model):
    user_name = models.CharField(max_length=100)
    user_department = models.CharField(max_length=100)
    user_designation = models.CharField(max_length=100)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    purpose = models.TextField()
    facilities_required = models.TextField()


#------------------------------------------------------------
#       FORMS
#------------------------------------------------------------

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ('user_name', 'user_department', 'user_designation', 'from_date', 'to_date', 'purpose', 'facilities_required')

