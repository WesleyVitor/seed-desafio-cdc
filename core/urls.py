from django.urls import path
from core.views import *

urlpatterns = [
    path("authors", AuthorCreate.as_view(), name="author_create"),
    path("categorys", CategoryCreate.as_view(), name="category_create"),
    path("books", BookListCreate.as_view(), name="book_create"),
    path("books/<int:pk>", BookDetailView.as_view(), name="book_detail"),
]
