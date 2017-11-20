from django.contrib import admin
from .models import Flows, WorkRequests, Tasks, TaskTemplates, Roles

# Register your models here.
admin.site.register(Flows)
admin.site.register(WorkRequests)
admin.site.register(Roles)
admin.site.register(TaskTemplates)
admin.site.register(Tasks)
