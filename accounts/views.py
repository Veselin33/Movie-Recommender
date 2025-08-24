from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomerCreationForm, LoginForm
from accounts.models import Customer


# Create your views here.


class CustomerRegisterView(CreateView):
    model = Customer
    form_class = CustomerCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('base')

class CustomerLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('base')

def logout_view(request):
    logout(request)
    return redirect('base')


