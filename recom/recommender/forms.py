
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class SearchForm(forms.Form):
    movie = forms.CharField(help_text="Enter movie(s) here")

    def clean_movie(self):
        data = self.cleaned_data['movie']
        # Remember to always return the cleaned data.
        return data
