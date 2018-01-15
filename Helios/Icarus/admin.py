from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
from Helios import resources

class RoleAdmin(ImportExportModelAdmin):
    resource_class = resources.RoleResource

class TTAdmin(ImportExportModelAdmin):
    resource_class = resources.TTResource

class PFAdmin(ImportExportModelAdmin):
    resource_class = resources.PFResource

# Register your models here.
admin.site.register(models.PFCat)
admin.site.register(models.Flows, PFAdmin)
admin.site.register(models.TaskTemplates, TTAdmin)
admin.site.register(models.Roles, RoleAdmin)

admin.site.register(models.WorkRequests)
admin.site.register(models.Tasks)
