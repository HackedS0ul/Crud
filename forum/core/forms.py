from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    isbn_number = forms.CharField(label="Barcode", required=False)
    name = forms.CharField(label="Book name")
    class Meta:
        model: Book
        fields = [
            'name',
            'isbn_number',
        ]