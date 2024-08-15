# pylint: disable=E1101:no-member

from datetime import datetime
from django.test import TestCase
from application.models import Task, User

class TaskTestCase(TestCase):

    def setUp(self) -> None:
        user = User.objects.create(
            username='Testes',
            name='Teste dos testes',
            email='teste@teste.com',
        )
        user.set_password("teste1234")
        user.save()

        Task.objects.create(
            user = user,
            title='task teste',
            description='task teste dos testes',
            due_date = datetime.now(),
            created_at= datetime.now(),
            updated_at = datetime.now()
        )


    def test_task_creation(self):
        task = Task.objects.get(user=1)
        self.assertEqual(task.title, 'task teste')
        self.assertEqual(task.due_date.day, datetime.now().day)
