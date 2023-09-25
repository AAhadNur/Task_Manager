from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from tasks.models import Task
from api.serializers import TaskViewSerializer, TaskCreateSerializer
from api.permissions import IsTaskOwner

# Create your views here.


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskViewSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()[:3]
    serializer_class = TaskCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsTaskOwner]

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskViewSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskViewSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
