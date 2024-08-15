# pylint: disable=E1101:no-member

from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from application.models import User, Task

class UpdateTaskAPIViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="1234"
        )

        self.task = Task.objects.create(
            user=self.user,
            title="Original Title",
            description="Original Description",
            due_date=timezone.now()
        )
        self.update_url = reverse('update_task_api', kwargs={'id': self.task.id})


    def test_update_task_authenticated(self):

        self.client.login(email='test@test.com', password='1234')
        updated_data = {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'due_date': timezone.now().isoformat(),
        }
        response = self.client.put(self.update_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, updated_data['title'])
        self.assertEqual(self.task.description, updated_data['description'])


    def test_update_task_unauthenticated(self):
        updated_data = {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'due_date': timezone.now().isoformat(),
        }
        response = self.client.put(self.update_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
