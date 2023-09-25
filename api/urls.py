from django.urls import path

from api import views


urlpatterns = [
    path('tasks/', views.TaskListView.as_view(),
         name='api-task-list'),
    path('tasks/create/', views.TaskCreateView.as_view(),
         name='api-task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDeleteView.as_view(),
         name='api-task-retrieve-update-delete'),
]
