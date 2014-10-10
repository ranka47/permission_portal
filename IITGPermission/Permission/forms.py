from Permission import models
from django.forms import ModelForm

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['user_name', 'user_department', 'user_designation', 'task_from_date', 'task_to_date', 'task_purpose', 'task_facilities',]
