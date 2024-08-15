# pylint: disable=E1101:no-member

from django.utils import timezone
from django.test import TestCase
from application.models import Task, User
from application.application_serializers.task_serializer import TaskSerialiser


class TaskSerializerTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="usertest",
            email="test@test.com",
            password="test1234"
        )
        self.task = Task.objects.create(
            user=self.user,
            title="Task test",
            description="This is a test task.",
            due_date=timezone.now(),
            created_at= timezone.now(),
            updated_at = timezone.now()
        )
        self.serializer = TaskSerialiser(instance=self.task)


    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set(
                ['id', 'title', 'description', 'due_date', 'created_at', 'updated_at']
            )
        )


    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.task.title)
        self.assertEqual(data['description'], self.task.description)
        self.assertEqual(data['due_date'][:10], self.task.due_date.isoformat()[:10])
        self.assertEqual(data['created_at'][:10], self.task.created_at.isoformat()[:10])
        self.assertEqual(data['updated_at'][:10], self.task.updated_at.isoformat()[:10] )


    def test_valid_data(self):
        valid_data = {
            'title': 'New Task',
            'description': 'New description',
            'due_date': timezone.now().isoformat(),
        }
        serializer = TaskSerialiser(data=valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['title'], 'New Task')
