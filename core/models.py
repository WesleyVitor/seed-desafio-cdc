from django.db import models
from django.contrib.auth.models import *
from datetime import datetime
# Create your models here.

class Author(models.Model):
    """
    Guarda informações sobre autores
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]

class Category(models.Model):
    """
    Guarda informações sobre categorias
    """

    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_name')
        ]
    
class Book(models.Model):
    """
    Guarda informações sobre livros
    """

    title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    resume = models.CharField(max_length=500, null=False, blank=False)
    sumary = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    numbers_of_pages = models.IntegerField(null=False, blank=False)
    isbn = models.CharField(max_length=100, null=False, blank=False, unique=True)
    publication_date = models.DateTimeField()

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False)



        

