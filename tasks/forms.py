from django import forms

from .models import Task


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
