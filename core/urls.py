from django.urls import path
from core.views import AuthorCreate

urlpatterns = [
    path("author", AuthorCreate.as_view(), name="author-create"),
]
