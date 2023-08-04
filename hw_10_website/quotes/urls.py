from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main"),
]
