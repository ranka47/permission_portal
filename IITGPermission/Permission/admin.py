from django.contrib import admin
from Permission import models

# Registering models into admin panel
admin.site.register(models.Task)
