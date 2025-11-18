from django import forms
from .models import Booklab


class BooklabForm(forms.ModelForm):
    class Meta:
        model = Booklab
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating']
