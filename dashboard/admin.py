from django.contrib import admin
from .models import Schemas


@admin.register(Schemas)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'title']
