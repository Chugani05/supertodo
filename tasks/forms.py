from django import forms

from .models import Task


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline')
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'id': 'post-title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

