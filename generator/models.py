from django.db import models


class FilesCSV(models.Model):
    date = models.DateField(auto_now_add=True)
    filename = models.CharField(max_length=255, verbose_name='File Name')
    user_id = models.BigIntegerField(verbose_name='User ID')
    schema_id = models.BigIntegerField(verbose_name='Schema ID')
    rows = models.IntegerField(verbose_name='Rows')
    status = models.BooleanField(verbose_name='Status', default=False)
    file = models.FileField(upload_to='data-csv/', blank=True)
