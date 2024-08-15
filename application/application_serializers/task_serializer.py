from rest_framework import serializers
from application.models import Task

class TaskSerialiser(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at =  serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'due_date',
            'created_at',
            'updated_at',
        )
