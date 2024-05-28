from django_virtual_models import VirtualModel

from core.models import *

class AuthorDetailVirtualModel(VirtualModel):
    class Meta:
        model = Author
        fields = ('name', 'description')

class CategoryDetailVirtualModel(VirtualModel):
    class Meta:
        model = Category
        fields = ('name',)

class BookDetailVirtualModel(VirtualModel):
    author = AuthorDetailVirtualModel(manager=Author.objects)
    category = CategoryDetailVirtualModel(manager=Category.objects)
    class Meta:
        model = Book
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