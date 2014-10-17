from django.contrib import admin
from Permission.models import Template, Group, Task

# Registering models into admin panel
# admin.site.register(models.Task)
class MembershipInline(admin.StackedInline):
    model = Template.hierarchies.through
    extra = 3


# class GroupAdmin(admin.ModelAdmin):
#     # inlines = [
#     #     MembershipInline,
#     # ]
#     pass

class TemplateAdmin(admin.ModelAdmin):
    
    inlines = [
        MembershipInline,
    ]

    fieldsets = [
    			(None,	{'fields':['name','description']}),

    ]
    exclude = ('hierarchies',)


	
# admin.site.register(Group, GroupAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Task)