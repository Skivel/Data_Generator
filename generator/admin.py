from django.contrib import admin
from .models import FilesCSV


class FilesAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'schema_id', 'status', 'rows']
    list_filter = ('user_id', 'date', 'rows', 'status')
    ordering = ('-date',)

admin.site.register(FilesCSV, FilesAdmin)
