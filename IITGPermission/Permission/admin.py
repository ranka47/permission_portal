from django.contrib import admin
from Permission import models
# Register your models here.



admin.site.register(models.Permission)
admin.site.register(models.Template)
admin.site.register(models.TaskUser)
admin.site.register(models.TaskGroup)
admin.site.register(models.Task)
