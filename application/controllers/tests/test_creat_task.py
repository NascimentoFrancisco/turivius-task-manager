# pylint: disable=E1101:no-member

from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from application.models import User, Task


class CreateTaskAPIViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="1234"
        )
        self.create_url = reverse('create_tastk_api')


    def test_create_task_authenticated(self):
        self.client.login(email='test@test.com', password='1234')
        data = {
            'title': 'Study Python',
            'description': 'Need Study Python',
            'due_date': timezone.now().isoformat(),
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Study Python')
        self.assertEqual(Task.objects.get().user, self.user)


    def test_create_task_unauthenticated(self):
        data = {
            'title': 'Study Python',
            'description': 'Need Study Python',
            'due_date': timezone.now().isoformat(),
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Task.objects.count(), 0)
