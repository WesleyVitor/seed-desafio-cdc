from core.models import *
from rest_framework.serializers import ModelSerializer

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", "email", "description")



