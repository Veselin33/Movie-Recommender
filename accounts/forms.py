from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from accounts.models import Customer


class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None

class CustomerChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Customer


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
