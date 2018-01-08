from import_export import resources
from import_export.admin import ImportExportModelAdmin
from Icarus import models

class RoleResource(resources.ModelResource):
    class Meta:
        model = models.Roles

class TTResource(resources.ModelResource):
    class Meta:
        model = models.TaskTemplates
