from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("signup/", views.SignUpUserView.as_view(), name="signup"),
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
]
