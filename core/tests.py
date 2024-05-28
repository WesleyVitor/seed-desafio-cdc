import datetime
import pytz

from unittest.mock import patch
from rest_framework.test import APITestCase
from django.urls import reverse
from core.models import Author
from model_bakery import baker

class AuthorCreateTest(APITestCase):
    def test_sucess_to_create_author_when_all_information_is_right(self):
        """
        Testa sucesso ao criar um autor quando todas as informações estão corretas
        """
        data = {
            "name": "Autor 1",
            "email": "autor@gmail.com",
            "description": "Descrição do autor"
        }
        url = reverse("author_create")
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 201)

        author_has_created = Author.objects.filter(email="autor@gmail.com").last()

        self.assertIsNotNone(author_has_created)
        self.assertEqual(author_has_created.name, "Autor 1")
        self.assertEqual(author_has_created.description, "Descrição do autor") 
    
    def test_fail_to_create_author_when_email_already_exists(self):
        """
        Testa falha ao criar um autor quando o email já existe
        """
        baker.make("core.Author", email="autor@gmail.com")
        data = {
            "name": "Autor 1",
            "email": "autor@gmail.com",
            "description": "Descrição do autor"
        }
        url = reverse("author_create")
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"email": ["Já existe um Autor com este email."]})
        
        amount_of_authors = Author.objects.filter(email="autor@gmail.com").count()
        self.assertEqual(amount_of_authors, 1)
    

class BookListCreateTest(APITestCase):

    def setUp(self) -> None:
        self.author = baker.make("core.Author")
        self.category = baker.make("core.Category")

    @patch("core.serializers.timezone")
    def test_error_to_create_book_without_obrigatories_items(self, mock_timezone):
        """
        Testa erro ao criar um livro sem título
        """
        now = datetime.datetime(2021, 1, 1).astimezone(pytz.timezone("America/Fortaleza"))
        mock_timezone.now.return_value = now
        data = {
            "resume": "Resumo do livro",
            "sumary": "Sumário do livro",
            "publication_date": '2021-01-01',
            "category": self.category.id,
            "author": self.author.id
        }
        url = reverse("book_create")
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, 400)
    
    @patch("core.serializers.timezone")
    def test_error_to_create_book_with_two_same_title(self, mock_timezone):
        """
        Testa erro ao criar um livro com dois livros com mesmo título
        """

        baker.make(
            "core.Book", 
            title="Livro 1", 
            resume="Resumo do livro", 
            sumary="Sumário do livro", 
            price=30.00, 
            numbers_of_pages=200, 
            isbn="1234567890", 
            publication_date='2021-01-01', 
            category=self.category, 
            author=self.author
        )  
        now = datetime.datetime(2021, 1, 1).astimezone(pytz.timezone("America/Fortaleza"))
        mock_timezone.now.return_value = now
        data = {
            "title":"Livro 1",
            "resume": "Resumo do livro",
            "sumary": "Sumário do livro",
            "price": 30.00,
            "numbers_of_pages": 200,
            "isbn": "1234567890",
            "publication_date": '2021-01-01',
            "category": self.category.id,
            "author": self.author.id
        }
        url = reverse("book_create")
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['title'][0]), "Já existe um livro com este título.")
        self.assertEqual(str(response.data['isbn'][0]), "Já existe um livro com este ISBN.")
    
    @patch("core.serializers.timezone")
    def test_error_to_create_book_with_price_less_than_20(self, mock_timezone):
        """
        Testa erro ao criar um livro com preço menor que 20
        """
        now = datetime.datetime(2021, 1, 1).astimezone(pytz.timezone("America/Fortaleza"))
        mock_timezone.now.return_value = now
        data = {
            "title":"Livro 1",
            "resume": "Resumo do livro",
            "sumary": "Sumário do livro",
            "price": 10.00,
            "numbers_of_pages": 200,
            "isbn": "1234567890",
            "publication_date": '2021-01-01',
            "category": self.category.id,
            "author": self.author.id
        }
        url = reverse("book_create")
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['price'][0]), "O preço do livro deve ser maior que 20.")
    @patch("core.serializers.timezone")
    def test_error_to_create_book_with_numbers_of_pages_less_than_100(self, mock_timezone):
        """
        Testa erro ao criar um livro com numbers_of_pages menor que 100
        """
        now = datetime.datetime(2021, 1, 1).astimezone(pytz.timezone("America/Fortaleza"))
        mock_timezone.now.return_value = now
        data = {
            "title":"Livro 1",
            "resume": "Resumo do livro",
            "sumary": "Sumário do livro",
            "price": 10.00,
            "numbers_of_pages": 20,
            "isbn": "1234567890",
            "publication_date": '2021-01-01',
            "category": self.category.id,
            "author": self.author.id
        }
        url = reverse("book_create")
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['numbers_of_pages'][0]), "O livro deve ter mais de 100 páginas.")
        
    @patch("core.serializers.timezone")
    def test_error_to_create_book_with_publication_date_less_than_now(self, mock_timezone):
        """
        Testa erro ao criar um livro com publication_date menor que 100
        """
        now = datetime.datetime(2021, 1, 1).astimezone(pytz.timezone("America/Fortaleza"))
        mock_timezone.now.return_value = now
        data = {
            "title":"Livro 1",
            "resume": "Resumo do livro",
            "sumary": "Sumário do livro",
            "price": 10.00,
            "numbers_of_pages": 20,
            "isbn": "1234567890",
            "publication_date": '2020-01-01',
            "category": self.category.id,
            "author": self.author.id
        }
        url = reverse("book_create")
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(str(response.data['publication_date'][0]), "A data de publicação não pode ser menor que a data atual.")

    def test_list_books(self):
        """
        Testa listagem de livros
        """

        baker.make(
            "core.Book", 
            title="Livro 1", 
            resume="Resumo do livro", 
            sumary="Sumário do livro", 
            price=30.00, 
            numbers_of_pages=200, 
            isbn="1234567890", 
            publication_date='2021-01-01', 
            category=self.category, 
            author=self.author
        )  
        
        url = reverse("book_create")
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

class BookDetailViewTest(APITestCase):
    def test_list_detail_of_book(self):
        """
        Testa detalhes de um livro
        """
        author = baker.make("core.Author", name="Autor 1", description="Descrição do autor")
        category = baker.make("core.Category")
        book = baker.make(
            "core.Book", 
            title="Livro 1", 
            resume="Resumo do livro", 
            sumary="Sumário do livro", 
            price=30.00, 
            numbers_of_pages=200, 
            isbn="1234567890", 
            publication_date='2021-01-01', 
            category=category, 
            author=author
        )  
        
        url = reverse("book_detail", kwargs={"pk": book.id})
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Livro 1")
        self.assertEqual(response.data['author']['name'], "Autor 1")
        self.assertEqual(response.data['author']['description'], "Descrição do autor")
        
    