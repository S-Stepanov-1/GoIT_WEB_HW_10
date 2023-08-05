from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import LoginForm


# Create your views here.
class LoginUserView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm
    # redirect_authenticated_user = True
    next_page = "/"


class SignUpUserView(CreateView):
    ...


class LogoutUserView(LogoutView):
    next_page = "/"
