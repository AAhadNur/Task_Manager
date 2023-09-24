
from django.urls import path

from tasks import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),


    path('task/<int:task_id>/delete-photo/<int:photo_id>/',
         views.delete_task_photo, name='delete-task-photo'),
]
