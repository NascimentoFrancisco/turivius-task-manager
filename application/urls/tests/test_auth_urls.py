from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from application.models import User


class JWTAuthenticationTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="1234"
        )
        self.token_url = reverse('token_obtain_pair')
        self.refresh_url = reverse('token_refresh')


    def test_obtain_jwt_token(self):
        response = self.client.post(self.token_url, {
            'email': 'test@test.com',
            'password': '1234',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


    def test_refresh_jwt_token(self):
        response = self.client.post(self.token_url, {
            'email': 'test@test.com',
            'password': '1234',
        })
        refresh_token = response.data['refresh']

        refresh_response = self.client.post(self.refresh_url, {
            'refresh': refresh_token,
        })
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', refresh_response.data)
