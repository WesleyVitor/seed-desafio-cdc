from django.urls import path
from core.views import *

urlpatterns = [
    path("authors", AuthorCreate.as_view(), name="author_create"),
    path("categorys", CategoryCreate.as_view(), name="category_create"),
    path("books", BookCreate.as_view(), name="book_create"),
]
