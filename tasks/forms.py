from django import forms

from .models import Task


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'}),
            'complete_before': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
