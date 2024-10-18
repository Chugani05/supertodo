from django import forms

from .models import Task


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline', 'check_box')
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
