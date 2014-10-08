from django.contrib import admin
from Permission.models import TaskUser,TaskGroup, Permission, Template
# Register your models here.



admin.site.register(Permission)
admin.site.register(Template)
admin.site.register(TaskUser)
admin.site.register(TaskGroup)
