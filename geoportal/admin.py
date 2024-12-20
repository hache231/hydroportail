from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import * 

# Register your models here.
class StationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...

admin.site.register(station, StationAdmin)
admin.site.register(product)
admin.site.register(source)
admin.site.register(service)
admin.site.register(type)
admin.site.register(Vendre)
admin.site.register(Fournir)
admin.site.register(Offrir)
admin.site.register(provinces)
admin.site.register(territories)
admin.site.register(sectors)
