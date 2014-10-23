from django.contrib import admin
from Permission.models import Template, Group, Task, TemplateGroup

class TemplateGroupInline(admin.TabularInline):

    model = TemplateGroup
    extra = 1

class TemplateAdmin(admin.ModelAdmin):
    inlines = [
        TemplateGroupInline,
    ]
    

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('user_name',)

# admin.site.register(Group, GroupAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(TemplateGroup)