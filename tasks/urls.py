
from django.urls import path

from tasks import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/create/', views.TaskCreateView.as_view(), name='create-task'),
    path('task/update/<int:pk>/', views.TaskUpdateView.as_view(), name='update-task'),
    path('task/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete-task'),

    path('task/<int:task_id>/delete-photo/<int:photo_id>/',
         views.delete_task_photo, name='delete-task-photo'),

    path('projects/', views.all_projects, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project'),
]
