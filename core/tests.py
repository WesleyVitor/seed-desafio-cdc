from rest_framework.test import APITestCase
from django.urls import reverse
from core.models import *
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

