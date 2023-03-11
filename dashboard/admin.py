from django.contrib import admin
from .models import Schemas


class SchemasAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_name', 'data_create', 'data_update')
    list_filter = ('user_name', 'data_create', 'data_update')
    search_fields = ('title', 'user_name')
    ordering = ('-data_create',)

admin.site.register(Schemas, SchemasAdmin)
