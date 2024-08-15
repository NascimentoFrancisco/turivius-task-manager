from django.test import TestCase
from application.models import User

class UserTestCase(TestCase):

    def setUp(self) -> None:
        user = User.objects.create(
            username='Testes',
            name='Teste dos testes',
            email='teste@teste.com',
        )
        user.set_password("teste1234")
        user.save()

    def test_model_create(self):
        user = User.objects.get(email="teste@teste.com")
        self.assertEqual(user.email, 'teste@teste.com')
        self.assertTrue(user.is_active)
