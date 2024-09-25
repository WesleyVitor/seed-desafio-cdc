from rest_framework import generics
from core.models import Author, Category, Book, Country, State
from core.serializers import StateSerializer, CountrySerializer, AuthorSerializer, CategorySerializer, BookSerializer, BookListSerializer, BookDetailSerializer

from django_virtual_models import VirtualModelRetrieveAPIView

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

class BookDetailView(VirtualModelRetrieveAPIView):
    """
    Detalha um Livro
    """
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    
    

class CountryCreate(generics.CreateAPIView):
    """
    Cria um novo país
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateCreate(generics.CreateAPIView):
    """
    Cria um novo país
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer