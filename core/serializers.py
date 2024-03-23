from core.models import *
from rest_framework import serializers 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", "email", "description")
    
    def validate_email(self, value):
        if Author.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email já cadastrado")
        return value



