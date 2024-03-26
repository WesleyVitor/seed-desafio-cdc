from rest_framework import generics
from core.models import *
from core.serializers import AuthorSerializer, CategorySerializer

class AuthorCreate(generics.CreateAPIView):
    """
    Cria um novo Autor
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryCreate(generics.CreateAPIView):
    """
    Cria uma nova Categoria
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
