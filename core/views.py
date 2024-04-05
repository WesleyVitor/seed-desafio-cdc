from rest_framework import generics
from core.models import *
from core.serializers import *

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

class BookListCreate(generics.ListCreateAPIView):
    """
    Cria e ler um novo Livro
    """
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookSerializer
        return BookListSerializer
    
    
