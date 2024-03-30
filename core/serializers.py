from core.models import *
from rest_framework import serializers 
#from core.validators import *
from rest_framework.validators import UniqueValidator
from django.utils import timezone

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", "email", "description")
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(queryset=Author.objects.all(), message="Já existe um Autor com este email.")
                ]
            }
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(queryset=Category.objects.all(), message="Já existe uma Categoria com este nome.")
                ]
            }
        }
    
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'resume', 'sumary', 'price', 'numbers_of_pages', 'isbn', 'publication_date', 'category', 'author')
        extra_kwargs = {
            'title': { 
                'validators': [
                    UniqueValidator(queryset=Book.objects.all(), message="Já existe um livro com este título.")
                ]
            },
            'isbn': {
                'validators': [
                    UniqueValidator(queryset=Book.objects.all(), message="Já existe um livro com este ISBN.")
                ]
            }
        }
    def validate_price(self, price):
        if price < 20:
            raise serializers.ValidationError("O preço do livro deve ser maior que 20.")
        return price
    
    def validate_numbers_of_pages(self, numbers_of_pages):
        if numbers_of_pages < 100:
            raise serializers.ValidationError("O livro deve ter mais de 100 páginas.")
        return numbers_of_pages

    def validate_publication_date(self, publication_date):
        now = timezone.now()
        
        if publication_date < now:
            raise serializers.ValidationError("A data de publicação não pode ser menor que a data atual.")
        
        return publication_date

