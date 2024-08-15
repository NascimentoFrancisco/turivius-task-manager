# pylint: disable=E1101:no-member

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from application.models import Task


class DeleteTaskAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_200_OK)
