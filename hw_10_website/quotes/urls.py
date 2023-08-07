from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main"),
    path("page/<int:page>", views.MainPageView.as_view(), name="paginator"),
    path("new_author", views.CreateAuthorView.as_view(), name="author"),
    path("new_quote", views.CreateQuoteView.as_view(), name="quote"),
    path("profile/<int:author_id>", views.ProfileView.as_view(), name="profile"),
    path("tag/<str:tag_name>", views.QuotesByTag.as_view(), name="tag"),
    path("tag/<str:tag_name>/page/<int:page>", views.QuotesByTag.as_view(), name="tag_paginator"),
]
