from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.views import CustomerRegisterView, CustomerLoginView, logout_view

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='register'),
    path('login/', CustomerLoginView.as_view(), name='login'),

    path('logout/', logout_view, name='logout'),
]