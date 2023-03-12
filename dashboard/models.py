from django.db import models


class Schemas(models.Model):
    user_id = models.BigIntegerField(verbose_name='User ID')
    user_name = models.CharField(max_length=255, verbose_name='User Name')
    title = models.CharField(max_length=255, verbose_name='Schema Title')
    separators = models.CharField(max_length=30, verbose_name='Column Separator', blank=True)
    character = models.CharField(max_length=30, verbose_name='String Character', blank=True)
    fields = models.JSONField(default=dict)
    data_create = models.DateField(auto_now_add=True, verbose_name='Data create')
    data_update = models.DateField(auto_now=True, verbose_name='Data update')

    def __str__(self):
        return self.title
