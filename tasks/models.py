from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=1500)
    slug = models.SlugField(unique=True, max_length=100)
    complete_before = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name