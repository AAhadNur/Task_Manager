from rest_framework import serializers
from tasks.models import Task


class TaskViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'created_by',
                  'project', 'creation_date', 'due_date', 'priority', 'is_complete']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description',
                  'project', 'due_date', 'priority', 'is_complete']
