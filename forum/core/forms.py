from django import forms
from .models import Book



IN_STORE = (
    ("YES", "Yes"),
    ("NO", "No"),
)
class BookForm(forms.Form):
    isbn_number = forms.CharField(label="Barcode", required=False)
    name = forms.CharField(label="Book name")
    description = forms.CharField(label="Short Description", max_length=500)
    author= forms.CharField(label="Author")
    in_store = forms.ChoiceField(label="In store", choices=IN_STORE)
    class Meta:
        model: Book
        fields = [
            'name',
            'isbn_number',
            'description',
            'author',
            'in_store',
        ]