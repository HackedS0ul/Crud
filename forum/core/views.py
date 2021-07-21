from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Book


#@method_decorator(login_required, name='dispatch')

class BookCreateView(CreateView):
    model = Book
    template_name = 'create.html'
    fields = ["name","isbn_number" ]
    success_url = "/"

class IndexView(ListView):
    model= Book
    template_name= 'listview.html'


class BookDetailView(DetailView):
    model = Book
    template_name = "details.html"

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'update.html'
    fields = ["name","isbn_number" ]
    success_url = "/"

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'delete.html'
    fields = ["name","isbn_number" ]
    success_url = "/"







