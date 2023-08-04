from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Quote, Tag, Author


# Create your views here.
class MainPageView(ListView):
    model = Quote
    template_name = "quotes/index.html"
    context_object_name = "quote_list"
    paginate_by = 10
