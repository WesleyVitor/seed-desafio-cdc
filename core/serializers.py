from core.models import Author, Category, Book, Country, State
from rest_framework import serializers 

from rest_framework.validators import UniqueValidator
from django.utils import timezone

from django_virtual_models import VirtualModelSerializer

from core.virtual_model import BookDetailVirtualModel

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

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title')
    
class AuthorDetailSerializer(VirtualModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'description')
    
class CategoryDetailSerializer(VirtualModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
    
class BookDetailSerializer(VirtualModelSerializer):
    author = AuthorDetailSerializer()
    category = CategoryDetailSerializer()
    class Meta:
        model = Book
        virtual_model = BookDetailVirtualModel
        fields = (
            'title',
            'resume',
            'sumary',
            'price',
            'numbers_of_pages',
            'isbn',
            'publication_date',
            'author',
            'category'
        )
    
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',) 
        extra_kwargs = {
            'name': { 
                'validators': [
                    UniqueValidator(queryset=Country.objects.all(), message="Já existe um país com este nome.")
                ]
            },
        }
    
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name','country') 
        extra_kwargs = {
            'name': { 
                'validators': [
                    UniqueValidator(queryset=Country.objects.all(), message="Já existe um estado com este nome.")
                ]
            },
        }

class PaymentSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    street = serializers.CharField(required=True)
    comp = serializers.CharField(required=True)
    document = serializers.CharField(required=True)
    document_type = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    cep = serializers.CharField(required=True)
    #city = serializers.PrimaryKeyRelatedField(queryset = City.objects.filter(active=True), required = True)
    country = serializers.PrimaryKeyRelatedField(queryset = Country.objects.all(), required = True)
    state = serializers.PrimaryKeyRelatedField(queryset = State.objects.all(), required = True)
    
            