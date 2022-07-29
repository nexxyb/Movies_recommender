
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class SearchForm(forms.Form):
    movie = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-1'
        self.helper.field_class = 'col-lg-11'
        #self.helper.add_input(Submit('submit', 'Search Movie'))
        

    def clean_movie(self):
        data = self.cleaned_data['movie']
        # Remember to always return the cleaned data.
        return data
