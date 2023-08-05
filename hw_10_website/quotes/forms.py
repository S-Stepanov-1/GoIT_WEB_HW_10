from django import forms
from django.forms import SelectDateWidget
from datetime import datetime
from .models import Author, Tag, Quote


class CustomSelectDateWidget(SelectDateWidget):
    def __init__(self, attrs=None, years=None, required=False):
        this_year = datetime.now().year
        if years is None:
            years = range(this_year, this_year - 100, -1)  # Годы в обратном порядке на 100 лет назад
        super().__init__(attrs, years, required)
        self.is_required = required


class AuthorCreateForm(forms.ModelForm):
    fullname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), required=False)
    born_date = forms.DateField(widget=CustomSelectDateWidget, required=False)
    born_location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    photo = forms.ImageField(required=False)

    class Meta:
        model = Author
        fields = ['fullname', 'description', 'born_date', 'born_location', 'photo']


class QuoteCreateForm(forms.ModelForm):
    quote = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    tags = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={"class": "form-control"}), queryset=Tag.objects.all())
    author = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "form-control"}), queryset=Author.objects.all())

    class Meta:
        model = Quote

        exclude = ["created"]
