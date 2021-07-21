

from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('create/', BookCreateView.as_view(), name="create"),
    path('details/<pk>/', BookDetailView.as_view(), name="view"),
    path('update/<pk>/', BookUpdateView.as_view(), name="update"),
    path('delete/<pk>/', BookDeleteView.as_view(), name="delete"),
    
]
