from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from appauth.forms import RegistrationForm

User = get_user_model()


class RegistrationView(CreateView):
    template_name = 'pages/registration.html'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
