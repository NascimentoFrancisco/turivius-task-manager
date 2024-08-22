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
        self.response = self.client.post(
            reverse("token_obtain_pair"),
            {'email':'test@test.com', 'password':'1234'}
        )

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.response.data['access']}")

        self.update_url = reverse('update_task_api', kwargs={'id': self.task.id})

        return super().setUp()


    def test_update_task_authenticated(self):

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
        self.client.credentials(HTTP_AUTHORIZATION="")
        updated_data = {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'due_date': timezone.now().isoformat(),
        }
        response = self.client.put(self.update_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
