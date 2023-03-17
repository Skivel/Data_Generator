import csv
import random

from django.conf import settings
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from faker import Faker

from dashboard.models import Schemas
from .models import FilesCSV


class DataGenerator(TemplateView):
    template_name = "data-generate.html"

    def post(self, *args, **kwargs):
        path = settings.BASE_DIR
        user_id = int(self.request.user.id)
        schema_id = int(kwargs['id'])
        num_rows = int(self.request.POST.get('rows'))

        schema = Schemas.objects.get(user_id=user_id, id=schema_id)
        column_names = list(schema.fields.keys())
        column_types = list(schema.fields.values())

        # Separators =
        if schema.separators == 'comma':
            sep = ','
        elif schema.separators == 'semicolon':
            sep = ';'
        elif schema.separators == 'tab':
            sep = '\t'
        elif schema.separators == 'pipe':
            sep = '|'
        elif schema.separators == 'tilde':
            sep = '~'
        else:
            sep = ' '

        # String Character =
        if schema.character == 'quote':
            char = "'"
        else:
            char = '"'

        def generate_column_data(column_type):
            if column_type == 'name':
                return fake.name()
            elif column_type == 'job':
                return fake.job()
            elif column_type == 'email':
                return fake.email()
            elif column_type == 'domain-name':
                return fake.domain_name()
            elif column_type == 'phone':
                return fake.phone_number()
            elif column_type == 'company':
                return fake.company()
            elif column_type == 'address':
                return fake.address()
            elif type(column_type) == list and column_type[0] == 'integer':
                return str(fake.random_int(min=int(column_type[1]), max=int(column_type[2])))
            elif type(column_type) == list and column_type[0] == 'text':
                randInt = random.randint(int(column_type[1]), int(column_type[2]))
                return fake.paragraph(nb_sentences=randInt)
            elif column_type == 'date':
                return fake.date()

        fake = Faker()
        model = FilesCSV(filename=schema.title, user_id=user_id, schema_id=schema_id, rows=num_rows)
        model.save()

        with open(f'{path}\\media\\csv\\{schema.title}_{schema_id}.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=column_names, delimiter=sep, quotechar=char)
            writer.writeheader()

            for row_index in range(num_rows):
                column_data = {}
                for column_index, column_name in enumerate(column_names):
                    column_type = column_types[column_index]
                    column_data[column_name] = generate_column_data(column_type)
                writer.writerow(column_data)

            csvfile.close()

        with open(f'{path}\\media\\csv\\{schema.title}_{schema_id}.csv', 'r') as csv_r:
            csv_result = csv_r.read()
        obj = get_object_or_404(FilesCSV, id=model.id)
        obj.status = True
        obj.file.save(f'{schema.title}_{model.id}.csv', ContentFile(csv_result))
        obj.save()

        return redirect('generator', self.request.user, schema_id)

    def get_context_data(self, **kwargs):
        user = self.request.user
        schema_id = kwargs['id']
        schema = Schemas.objects.get(user_id=user.id, id=schema_id)
        dict_keys = list(schema.fields.keys())
        dict_values = list(schema.fields.values())
        dict_arr = {}
        for i, value in enumerate(dict_values):
            if dict_values[i] == 'name':
                dict_values[i] = "Full Name"

            if dict_values[i] == 'job':
                dict_values[i] = 'Job'

            if dict_values[i] == 'domain-name':
                dict_values[i] = 'Domain Name'

            if dict_values[i] == 'company':
                dict_values[i] = 'Company'

            if dict_values[i] == 'address':
                dict_values[i] = 'Address'

            if type(dict_values[i]) == list and dict_values[i][0] == 'integer':
                dict_values[i] = "Integer"

            if type(dict_values[i]) == list and dict_values[i][0] == 'text':
                dict_values[i] = "Text"

            if dict_values[i] == 'email':
                dict_values[i] = 'Email'

            if dict_values[i] == 'phone':
                dict_values[i] = 'Phone'

            if dict_values[i] == 'date':
                dict_values[i] = 'Date'

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


def downloadCSV(request, *args, **kwargs):
    file_id = kwargs['file_id']
    file = get_object_or_404(FilesCSV, id=file_id)
    response = HttpResponse(file.file)
    response['Content-Disposition'] = f'attachment; filename="{file.filename}.csv"'
    return response