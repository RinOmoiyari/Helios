from import_export import resources
from import_export.admin import ImportExportModelAdmin
from Icarus import models

class PFCResource(resources.ModelResource):
    class Meta:
        model = models.PFCat

class PFResource(resources.ModelResource):
    class Meta:
        model = models.Flows

class TTResource(resources.ModelResource):
    class Meta:
        model = models.TaskTemplates

class InstResource(resources.ModelResource):
    class Meta:
        model = models.Institutions

class ColResource(resources.ModelResource):
    class Meta:
        model = models.Colleges

class SchResource(resources.ModelResource):
    class Meta:
        model = models.Schools

class CrsResource(resources.ModelResource):
    class Meta:
        model = models.Courses

class CvsResource(resources.ModelResource):
    class Meta:
        model = models.CourseVersions

class RoleResource(resources.ModelResource):
    class Meta:
        model = models.Roles

class WRResource(resources.ModelResource):
    class Meta:
        model = models.WorkRequests

class TaskResource(resources.ModelResource):
    class Meta:
        model = models.Tasks
