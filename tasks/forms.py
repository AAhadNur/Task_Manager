from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description',
                  'due_date', 'priority', 'is_complete']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TaskPhotoUploadForm(forms.Form):
    photo = forms.ImageField(widget=forms.ClearableFileInput)
