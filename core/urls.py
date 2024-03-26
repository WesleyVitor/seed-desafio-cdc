from django.urls import path
from core.views import *

urlpatterns = [
    path("author", AuthorCreate.as_view(), name="author_create"),
    path("category", CategoryCreate.as_view(), name="category_create"),
]
