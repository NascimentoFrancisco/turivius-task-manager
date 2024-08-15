# pylint: disable=E1101:no-member

from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from application.models import User, Task

class DeleteTaskAPIViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="1234"
        )
        self.task = Task.objects.create(
            user=self.user,
            title="Task test delete",
            description="Description task delete",
            due_date=timezone.now()
        )
        self.delete_url = reverse('delete_task_api', kwargs={'id': self.task.id})

    def test_delete_task_authenticated(self):
        self.client.login(email='test@test.com', password='1234')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Task deleted successfully."})
        self.assertEqual(Task.objects.count(), 0)

    def test_delete_task_unauthenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Task.objects.count(), 1)

    def test_delete_task_not_found(self):
        self.client.login(email='test@test.com', password='1234')
        url = reverse('delete_task_api', kwargs={'id': 9999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Task.objects.count(), 1)
