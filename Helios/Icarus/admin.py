from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
from Helios import resources

class PFCAdmin(ImportExportModelAdmin):
    resource_class = resources.PFCResource

class PFAdmin(ImportExportModelAdmin):
    resource_class = resources.PFResource

class TTAdmin(ImportExportModelAdmin):
    resource_class = resources.TTResource

class InstAdmin(ImportExportModelAdmin):
    resource_class = resources.InstResource

class ColAdmin(ImportExportModelAdmin):
    resource_class = resources.ColResource

class SchAdmin(ImportExportModelAdmin):
    resource_class = resources.SchResource

class CrsAdmin(ImportExportModelAdmin):
    resource_class = resources.CrsResource

class CvsAdmin(ImportExportModelAdmin):
    resource_class = resources.CvsResource

class RoleAdmin(ImportExportModelAdmin):
    resource_class = resources.RoleResource


class WRAdmin(ImportExportModelAdmin):
    resource_class = resources.WRResource

class TaskAdmin(ImportExportModelAdmin):
    resource_class = resources.TaskResource


# Register your models here.
admin.site.register(models.PFCat,PFCAdmin)
admin.site.register(models.Flows, PFAdmin)
admin.site.register(models.TaskTemplates, TTAdmin)

admin.site.register(models.Institutions, InstAdmin)
admin.site.register(models.Colleges, ColAdmin)
admin.site.register(models.Schools, SchAdmin)
admin.site.register(models.Courses, CrsAdmin)
admin.site.register(models.CourseVersions, CvsAdmin)
admin.site.register(models.Roles, RoleAdmin)

admin.site.register(models.WorkRequests, WRAdmin )
admin.site.register(models.Tasks, TaskAdmin)
