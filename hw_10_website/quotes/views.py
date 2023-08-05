from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse

from .models import Quote, Tag, Author
from .forms import AuthorCreateForm, QuoteCreateForm


# Create your views here.
class MainPageView(ListView):
    model = Quote
    template_name = "quotes/index.html"
    context_object_name = "quote_list"
    paginate_by = 5
    ordering = "-created"


class CreateAuthorView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = "quotes/author.html"
    form_class = AuthorCreateForm

    def get_success_url(self):
        return reverse("quotes:main")


class CreateQuoteView(LoginRequiredMixin, CreateView):
    model = Quote
    template_name = "quotes/quote.html"
    form_class = QuoteCreateForm

    def get_success_url(self):
        return reverse("quotes:main")
