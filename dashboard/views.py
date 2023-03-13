from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
import json

from .models import Schemas
from generator.models import FilesCSV


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        username = self.request.user
        data = Schemas.objects.filter(user_id=username.id)

        context = {
            'user_name': username,
            'data': data
        }
        return context


class CreateSchemaView(TemplateView):
    template_name = 'dashboard-create.html'

    def post(self, *args, **kwargs):
        user = self.request.user
        name = self.request.POST['name']
        separators = self.request.POST['separators']
        character = self.request.POST['character']
        keys = self.request.POST.getlist('dynamic-key[]')
        values = self.request.POST.getlist('dynamic-value[]')
        integer_values = self.request.POST.getlist('integer-value[]')
        text_values = self.request.POST.getlist('text-value[]')
        integer_values.insert(0, 'integer')
        text_values.insert(0, 'text')
        JSON_result = {}
        for i in range(len(keys)):
            if values[i] == 'integer':
                JSON_result.update({keys[i]: integer_values})
            elif values[i] == 'text':
                JSON_result.update({keys[i]: text_values})
            else:
                JSON_result.update({keys[i]: values[i]})

        model = Schemas(user_id=user.id, user_name=user, title=name, separators=separators, character=character, fields=JSON_result)
        model.save()
        return redirect("home", user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user
        return context


class EditSchemaView(TemplateView):
    template_name = 'dashboard-edit.html'

    def get_context_data(self, **kwargs):
        id_schema = self.kwargs['id']
        schema = Schemas.objects.get(id=id_schema)
        data = schema.fields
        context = {
            'user_name': self.request.user,
            'data_keys': json.dumps(list(data.keys())),
            'data_values': json.dumps(list(data.values())),
            'schema': schema
        }
        return context

    def post(self, request, **kwargs):
        user = request.user
        name = request.POST['name']
        separators = request.POST['separators']
        character = request.POST['character']
        keys = request.POST.getlist('dynamic-key[]')
        values = request.POST.getlist('dynamic-value[]')
        integer_values = request.POST.getlist('integer-value[]')
        text_values = request.POST.getlist('text-value[]')
        integer_values.insert(0, 'integer')
        text_values.insert(0, 'text')
        JSON_result = {}
        for i in range(len(keys)):
            if values[i] == 'integer':
                JSON_result.update({keys[i]: integer_values})
            elif values[i] == 'text':
                JSON_result.update({keys[i]: text_values})
            else:
                JSON_result.update({keys[i]: values[i]})

        schema_id = self.kwargs['id']
        schema = get_object_or_404(Schemas, id=schema_id, user_id=user.id)
        schema.title = name
        schema.separators = separators
        schema.character = character
        schema.fields = JSON_result
        schema.save()
        return redirect("home", user)


def deleteSchema(request, **kwargs):
    userId = request.user.id
    schemaId = kwargs["id"]

    userSchema = Schemas.objects.filter(user_id=userId, id=schemaId)
    userSchemaDataSets = FilesCSV.objects.filter(user_id=userId, schema_id=schemaId)
    userSchema.delete()
    userSchemaDataSets.delete()
    return redirect('home', request.user)


def logout_view(request):
    logout(request)
    return redirect('login')