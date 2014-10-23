from Permission import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _


class TaskForm(ModelForm):
    """
    TaskForm genrated form from models. Refer to ModelForms in djangoproject.com
    """
    # current_group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    to_date = forms.DateTimeField(widget=SelectDateWidget)
    from_date = forms.DateTimeField(widget=SelectDateWidget)
    # to_date = forms.TimeField(widget=SelectTimeWidget())

    class Meta:
        model = models.Task
        fields = ('template_id', 'subject', 'user_department', 'user_designation', 'from_date', 'to_date', 'purpose', 'facilities_required')


class TaskFormSubmitted(ModelForm):
    """
    TaskFormSubmitted generated after form is submitted to take permissions from different levels of
    hierarchy
    """

class CommentForm(ModelForm):
    text = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter Comment'}))
    class Meta:
        model = models.Comment
        fields = ('text',)

# class TemplateForm(ModelForm):
#   class Meta:
#       model = models.Template
#       fields = ('name','description','hierarchy_1','hierarchy_2','hierarchy_3','hierarchy_4','hierarchy_5')