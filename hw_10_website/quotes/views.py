from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse
from django.shortcuts import get_object_or_404


from .models import Quote, Author
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


class ProfileView(DetailView):
    model = Author
    template_name = "quotes/profile.html"
    context_object_name = "author"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("author_id")
        return get_object_or_404(Author, id=pk)
