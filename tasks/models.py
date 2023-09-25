from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class Task(models.Model):

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Meidum'),
        (HIGH, 'High'),
    ]

    project = models.ForeignKey(
        Project, related_name='tasks', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default=MEDIUM)
    is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title


class TaskPhoto(models.Model):
    task = models.ForeignKey(
        'Task', related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='task_photos/')
