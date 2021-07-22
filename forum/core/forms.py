from django import forms
from .models import Book


class BookForm(forms.Form):
    isbn_number = forms.CharField(label="Barcode", required=False)
    name = forms.CharField(label="Book name")
