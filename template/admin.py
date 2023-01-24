from django.contrib import admin
from template.models import Template
from import_export.admin import ImportExportMixin

class TemplateAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
            'name',
            'desc',
    )
    list_display_links = ('name',)
    search_fields = ('name', 'desc')


admin.site.register(Template, TemplateAdmin)

# Register your models here.
