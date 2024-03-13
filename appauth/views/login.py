import django.contrib.auth.views

from appauth.forms import LoginForm


class LoginView(django.contrib.auth.views.LoginView):
    template_name = 'pages/login.html'
    form_class = LoginForm

