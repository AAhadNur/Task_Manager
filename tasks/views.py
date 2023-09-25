from typing import Any
from django.utils import timezone
from datetime import date
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect

from tasks.models import Task, TaskPhoto, Project
from tasks.forms import TaskPhotoUploadForm, TaskForm
from tasks.mixins import OwnerRequiredMixin

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/home.html'
    paginate_by = 6
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.all()

        created_at = self.request.GET.get('created_at')

        if created_at == 'today':
            yesterday = date.today() - timedelta(days=1)
            queryset = queryset.filter(creation_date__gt=yesterday)
        elif created_at == 'previous_day':
            yesterday = date.today() - timedelta(days=1)
            queryset = queryset.exclude(creation_date__gt=date.today()).filter(
                creation_date__gte=yesterday)
        elif created_at == 'last_7_days':
            seven_days_ago = timezone.now() - timedelta(days=7)
            queryset = queryset.filter(creation_date__gte=seven_days_ago)
        elif created_at == 'last_month':
            last_month = timezone.now() - timedelta(days=30)
            queryset = queryset.filter(creation_date__gte=last_month)

        due_date = self.request.GET.get('due_date')

        if due_date == 'next_day':
            next_day = timezone.now() + timedelta(days=1)
            queryset = queryset.filter(
                due_date__gte=date.today()).filter(due_date__lt=next_day)

        elif due_date == 'next_3_day':
            next_day = timezone.now() + timedelta(days=3)
            queryset = queryset.exclude(
                due_date__lte=date.today()).filter(due_date__lt=next_day)

        elif due_date == 'next_7_day':
            next_day = timezone.now() + timedelta(days=7)
            queryset = queryset.exclude(
                due_date__lte=date.today()).filter(due_date__lt=next_day)

        elif due_date == 'next_30_day':
            next_day = timezone.now() + timedelta(days=30)
            queryset = queryset.exclude(
                due_date__lte=date.today()).filter(due_date__lt=next_day)

        priority = self.request.GET.get('priority')

        if priority:
            queryset = queryset.filter(priority=priority)

        is_complete = self.request.GET.get('is_complete')
        if is_complete == 'true':
            queryset = queryset.filter(is_complete=True)
        elif is_complete == 'false':
            queryset = queryset.filter(is_complete=False)

        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )

        return queryset


class TaskDetailView(DetailView, FormView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
    form_class = TaskPhotoUploadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()

        task_photos = task.photos.all()

        context['task_photos'] = task_photos

        return context

    def form_valid(self, form):
        task = self.get_object()
        photo = self.request.FILES.get('photo')

        if photo:
            task_photo = TaskPhoto(task=task, photo=photo)
            task_photo.save()
            messages.success(self.request, 'Uploaded a new photo')
        else:
            messages.error(self.request, 'You did not select any photo')

        return HttpResponseRedirect(reverse('task-detail', kwargs={'pk': task.pk}))


# function based view of deleting task's photos
def delete_task_photo(request, task_id, photo_id):
    task = get_object_or_404(Task, pk=task_id)
    photo = get_object_or_404(TaskPhoto, pk=photo_id)

    if photo.task == task:
        photo.delete()
        messages.success(request, 'Photo Deleted')

    return redirect('task-detail', pk=task.pk)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(
            self.request, f'{self.request.user.username} Created a new Task')
        return reverse('task-detail', kwargs={'pk': self.object.pk})


class TaskUpdateView(OwnerRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Task updated successfully ...')
        return reverse('task-detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(OwnerRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Task deleted...')
        return reverse('home')


def all_projects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    return render(request, 'tasks/projects.html', context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    tasks = Task.objects.filter(project=project)

    context = {
        'project': project,
        'tasks': tasks,
    }
    return render(request, 'tasks/project_detail.html', context)
