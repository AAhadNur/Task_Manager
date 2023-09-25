from rest_framework import generics, permissions

from tasks.models import Task
from api.serializers import TaskSerializer

# Create your views here.


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()[:3]
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
