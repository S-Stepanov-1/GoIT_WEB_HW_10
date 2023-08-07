from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Count


from .models import Quote, Author, QuoteTag, Tag
from .forms import AuthorCreateForm, QuoteCreateForm


# Create your views here.
class CustomMixIn:
    model = Quote
    template_name = "quotes/index.html"
    context_object_name = "quote_list"
    ordering = "-created"
    paginate_by = 10

    def top_tags(self):
        top_tags_id = QuoteTag.objects.values('tag_id').annotate(tag_count=Count('tag_id')).order_by('-tag_count')[:10]

        top_tags_name = []
        for tag in top_tags_id:
            top_tags_name.append(Tag.objects.get(id=tag["tag_id"]))

        return top_tags_name


class MainPageView(CustomMixIn, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["top_tags"] = self.top_tags()
        return context


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


class QuotesByTag(CustomMixIn, ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["top_tags"] = self.top_tags()
        return context

    def get_queryset(self):
        tag_name = self.kwargs["tag_name"]
        tag_object = Tag.objects.get(name=tag_name)

        quotes = Quote.objects.filter(tags=tag_object)
        return quotes
