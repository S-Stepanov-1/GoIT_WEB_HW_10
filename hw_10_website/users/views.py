from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from .forms import LoginForm, SignUpForm


# Create your views here.
class LoginUserView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm
    next_page = "/"


class SignUpUserView(CreateView):
    template_name = "users/signup.html"
    form_class = SignUpForm

    def get_success_url(self):
        return reverse("users:login")


class LogoutUserView(LogoutView):
    next_page = "/"



