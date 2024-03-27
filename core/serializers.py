from core.models import *
from rest_framework import serializers 
#from core.validators import *
from rest_framework.validators import UniqueValidator


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



