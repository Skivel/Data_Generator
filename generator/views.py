import csv

from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from faker import Faker

from dashboard.models import Schemas
from .models import FilesCSV


class DataGenerator(TemplateView):
    template_name = "data-generate.html"

    def post(self, *args, **kwargs):
        user_id = int(self.request.user.id)
        schema_id = int(kwargs['id'])
        num_rows = int(self.request.POST.get('rows'))

        schema = Schemas.objects.get(user_id=user_id, id=schema_id)
        column_names = list(schema.fields.keys())
        column_types = list(schema.fields.values())

        def generate_column_data(column_type):
            if column_type == 'full-name':
                return fake.name()
            elif type(column_type) == list:
                return str(fake.random_int(min=5, max=8))
            elif column_type == 'email':
                return fake.email()
            elif column_type == 'phone':
                return fake.phone_number()
            elif column_type == 'city':
                return fake.city()

        fake = Faker()

        with open(f'{schema.title}.txt', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=column_names)
            writer.writeheader()

            for row_index in range(num_rows):
                column_data = {}
                for column_index, column_name in enumerate(column_names):
                    column_type = column_types[column_index]
                    column_data[column_name] = generate_column_data(column_type)
                writer.writerow(column_data)

        csvfile.close()

        model = FilesCSV(user_id=user_id, schema_id=schema_id, rows=num_rows)
        model.save()

        return redirect('generator', self.request.user, schema_id)

    def get_context_data(self, **kwargs):
        user = self.request.user
        schema_id = kwargs['id']
        schema = Schemas.objects.get(user_id=user.id, id=schema_id)
        dict_keys = list(schema.fields.keys())
        dict_values = list(schema.fields.values())
        dict_arr = {}
        for i, value in enumerate(dict_values):
            if dict_values[i] == 'full-name':
                dict_values[i] = "Full Name"

            if type(dict_values[i]) == list:
                dict_values[i] = "Integer"

            if dict_values[i] == 'email':
                dict_values[i] = 'Email'

            if dict_values[i] == 'phone':
                dict_values[i] = 'Phone'

            if dict_values[i] == 'city':
                dict_values[i] = 'City'

        for i in range(len(dict_keys)):
            dict_arr.update({dict_keys[i]: dict_values[i]})

        dict_files = FilesCSV.objects.filter(user_id=user.id, schema_id=schema_id)

        context = {
            'user_name': user,
            'schema_id': schema_id,
            'schema': schema,
            'dict': dict_arr,
            'files': dict_files
        }
        return context


def downloadCSV(**kwargs):
    file_id = kwargs['file_id']
    file = get_object_or_404(FilesCSV, id=file_id)
    response = HttpResponse(file.file, content_type=file.content_type)
    response['Content-Disposition'] = f'attachment; filename="{file.filename}"'
    return response