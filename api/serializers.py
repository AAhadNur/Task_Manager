from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'created_by',
                  'project', 'due_date', 'priority', 'is_complete']
