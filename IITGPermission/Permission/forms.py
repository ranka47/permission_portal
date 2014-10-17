from Permission import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm

class TaskForm(ModelForm):
    """
    TaskForm genrated form from models. Refer to ModelForms in djangoproject.com
    """
    class Meta:
        model = models.Task
        fields = ('template_id','user_department', 'user_designation', 'from_date', 'to_date', 'purpose', 'facilities_required')



