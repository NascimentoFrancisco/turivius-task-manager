# pylint: disable=E1101:no-member

from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from application.models import User, Task


class GetAllTaskAPIViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="1234"
        )
        self.task1 = Task.objects.create(
            user=self.user,
            title="Task 1",
            description="Task 1 description",
            due_date=timezone.now()
        )
        self.task2 = Task.objects.create(
            user=self.user,
            title="Tarefa 2",
            description="Task 2 description",
            due_date=timezone.now()
        )
        self.get_all_url = reverse('get_all_task_api')

    def test_get_all_tasks_authenticated(self):
        self.client.login(email='test@test.com', password='1234')
        response = self.client.get(self.get_all_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], self.task1.title)
        self.assertEqual(response.data[1]['title'], self.task2.title)

    def test_get_all_tasks_unauthenticated(self):
        response = self.client.get(self.get_all_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
