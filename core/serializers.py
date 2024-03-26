from core.models import *
from rest_framework import serializers 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", "email", "description")
    
    def validate_email(self, value):
        if Author.objects.filter(email=value).exists():
            raise serializers.ValidationError(f"Já existe um Author(a) com o e-mail {value} já cadastrado.")
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)
    
    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError(f"Já existe uma Categoria com o nome {value} já cadastrado.")
        return value



