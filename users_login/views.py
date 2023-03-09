from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse

from users_login.forms import LoginForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        user = self.request.user
        url = reverse('home', args=[user])
        return url