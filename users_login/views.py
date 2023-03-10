from django.contrib.auth.views import LoginView
from django.urls import reverse

from users_login.forms import LoginForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        user = self.request.user
        url = reverse('home', args=[user])
        return url