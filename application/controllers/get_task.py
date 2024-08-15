# pylint: disable=E1101:no-member
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from application.models import Task
from application.application_serializers.task_serializer import TaskSerialiser


class RetrieveTaskAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerialiser
    queryset = Task.objects.all()
