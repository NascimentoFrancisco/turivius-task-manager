# pylint: disable=E1101:no-member
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from application.models import User, Task

class RetrieveTaskAPIViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="1234"
        )
        self.task = Task.objects.create(
            user=self.user,
            title="Task test",
            description="Task description",
            due_date=timezone.now()
        )
        self.response = self.client.post(
            reverse("token_obtain_pair"),
            {'email':'test@test.com', 'password':'1234'}
        )

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.response.data['access']}")
        self.retrieve_url = reverse('retrieve_task_api', kwargs={'pk': self.task.id})

        return super().setUp()


    def test_retrieve_task_authenticated(self):
        response = self.client.get(self.retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.task.id)
        self.assertEqual(response.data['title'], self.task.title)
        self.assertEqual(response.data['description'], self.task.description)


    def test_retrieve_task_not_found(self):
        self.client.login(email='test@test.com', password='1234')
        url = reverse('retrieve_task_api', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_retrieve_task_unauthenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.get(self.retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
