from Permission import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
# from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _
# from Permission import selecttimewidget
# from bootstrap3_datetime.widgets import DateTimePicker
import datetime

class TaskForm(forms.ModelForm):
    # urgency = forms.DateTimeField(required=False, widget=DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime":False}))
    class Meta:
        model=models.Task
        exclude=('applicant','date_of_application','status','status_description')
        widgets = {
        'urgency' : SelectDateWidget(years=range(datetime.datetime.now().year, datetime.datetime.now().year + 2)),
        'description':forms.Textarea(attrs={'rows':6,}),
        'special_mentions':forms.Textarea(attrs={'rows':6,}),
        
        }

class CommentForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Enter your comment', 'rows':3, 'cols':40}))
    class Meta:
        model = models.Comment
        fields = ('text',)
