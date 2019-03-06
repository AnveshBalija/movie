from django import forms
from testapp.models import Movie
from django.core import validators

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'