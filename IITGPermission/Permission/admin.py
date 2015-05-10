from django.contrib import admin
from Permission import models

# class TemplateUserInline(admin.TabularInline):

#     model = TemplateUser
#     extra = 1

# class TemplateAdmin(admin.ModelAdmin):
#     inlines = [
#         TemplateUserInline,
#     ]
    

# class TaskAdmin(admin.ModelAdmin):
#     readonly_fields = ('user_name',)

# # admin.site.register(Group, GroupAdmin)
# admin.site.register(Template, TemplateAdmin)
# admin.site.register(Task,TaskAdmin)
# admin.site.register(TemplateUser)

admin.site.register(models.Task)