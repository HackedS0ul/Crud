from django import forms
from .models import Book


class BookForm(forms.Form):
    isbn_number = forms.CharField(label="Barcode", required=False)
    name = forms.CharField(label="Book name")
    description = forms.CharField(label="Short Description")
    class Meta:
        model: Book
        fields = [
            'name',
            'isbn_number',
            'description',
        ]