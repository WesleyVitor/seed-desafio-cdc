from rest_framework import generics
from core.models import Author
from core.serializers import AuthorSerializer

class AuthorCreate(generics.CreateAPIView):
    """
    Cria um novo Autor
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
