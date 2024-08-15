from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from application.application_serializers.task_serializer import TaskSerialiser


class CreateTaskAPIView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerialiser

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
