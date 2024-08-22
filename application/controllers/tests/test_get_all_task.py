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

        self.response = self.client.post(
            reverse("token_obtain_pair"),
            {'email':'test@test.com', 'password':'1234'}
        )

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.response.data['access']}")

        self.get_all_url = reverse('get_all_task_api')

        return super().setUp()


    def test_get_all_tasks_authenticated(self):
        response = self.client.get(self.get_all_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], self.task1.title)
        self.assertEqual(response.data[1]['title'], self.task2.title)


    def test_get_all_tasks_unauthenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(self.get_all_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
