# pylint: disable=E1101:no-member

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from application.models import Task
from application.application_serializers.task_serializer import TaskSerialiser


class UpdateTaskAPIView(generics.UpdateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser
    lookup_field = 'id'
