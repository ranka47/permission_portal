from Permission import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from Permission import selecttimewidget


class TaskForm(ModelForm):
    """
    TaskForm genrated form from models. Refer to ModelForms in djangoproject.com
    """
    # current_group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    from_date = forms.DateField(widget=SelectDateWidget)
    from_time =forms.TimeField(widget=selecttimewidget.SelectTimeWidget())
    to_date = forms.DateField(widget=SelectDateWidget)
    to_time = forms.TimeField(widget=selecttimewidget.SelectTimeWidget())

    class Meta:
        model = models.Task
        fields = ('template_id','user_department', 'user_designation', 'from_date', 'from_time','to_date','to_time', 'purpose', 'facilities_required')


class TaskFormSubmitted(ModelForm):
	"""
	TaskFormSubmitted generated after form is submitted to take permissions from different levels of
	hierarchy
	"""
	

# class TemplateForm(ModelForm):
# 	class Meta:
# 		model = models.Template
# 		fields = ('name','description','hierarchy_1','hierarchy_2','hierarchy_3','hierarchy_4','hierarchy_5')



