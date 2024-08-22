# pylint: disable=E1101:no-member
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from application.models import User, Task


class TestCaseCreateTaskAPIView(APITestCase):


    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="1234"
        )

        response = self.client.post(
            reverse("token_obtain_pair"),
            {'email':'test@test.com', 'password':'1234'}
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

        return super().setUp()


    def test_create_task_authenticated(self):
        data = {
            'title': 'Study Python',
            'description': 'Need Study Python',
            'due_date': timezone.now(),
        }

        response = self.client.post(reverse("create_task_api"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Study Python')
        self.assertEqual(Task.objects.get().user, self.user)


    def test_create_task_unauthenticated(self):
        data = {
            'title': 'Study Python',
            'description': 'Need Study Python',
            'due_date': timezone.now(),
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {'fdsfsa'}")
        response = self.client.post(reverse("create_task_api"), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Task.objects.count(), 0)
