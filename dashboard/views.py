from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from django.shortcuts import render
from .models import Schemas


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


def logout_view(request):
    logout(request)
    return redirect('login')


class CreateSchemaView(TemplateView):
    template_name = 'dashboard-create.html'


def my_view(request, *args, **kwargs):
    user = request.user
    if request.method == 'POST':
        name = request.POST['name']
        keys = request.POST.getlist('dynamic-key[]')
        values = request.POST.getlist('dynamic-value[]')
        print(keys)
        print(values)
        JSON_result = {keys[i]: values[i] for i in range(len(keys))}
        print(JSON_result)

        model = Schemas(user_id=user.id, user_name=user, title=name, fields=JSON_result)
        model.save()
        return redirect("home", user)
    else:
        return render(request, 'dashboard-create.html', {'user_name': user})


def deleteSchema(request, *args, **kwargs):
    userId = request.user.id
    schemaId = kwargs["id"]

    userSchema = Schemas.objects.filter(user_id=userId, id=schemaId)
    userSchema.delete()
    return redirect('home', request.user)