from django.views.generic import CreateView
from django.urls import reverse_lazy
from acme_project.acme_project.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration_form.html'

