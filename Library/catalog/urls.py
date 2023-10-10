from django.urls import path
from . import views

app_name= 'catalog'

urlpatterns = [
    path("", views.index, name='index'),
    path("add-book/", views.BookCreateView.as_view(), name='add_book'),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name='book_detail'),
]

