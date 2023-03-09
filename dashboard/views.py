from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        username = self.request.user

        context = {
            'user_name': username
        }
        return context


def logout_view(request):
    logout(request)
    return redirect('login')


class CreateSchemaView(TemplateView):
    template_name = 'dashboard-create.html'
