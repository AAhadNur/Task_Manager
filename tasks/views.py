from django.utils import timezone
from datetime import date
from datetime import timedelta
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from tasks.models import Task

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'
    paginate_by = 6

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
