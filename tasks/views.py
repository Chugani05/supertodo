from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddPostForm
from .models import Task


def task_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, 'tasks/task-list.html', dict(tasks=tasks))


def done_task(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.filter(check_box=True)
    return render(request, 'tasks/task-list.html', dict(tasks=tasks))


def pending_task(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.filter(check_box=False)
    return render(request, 'tasks/task-list.html', dict(tasks=tasks))


def task_detail(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task/task-detail.html', dict(task=task))


def add_task(request):
    if request.method == 'POST':
        if (form := AddPostForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.title)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = AddPostForm()
    return render(request, 'tasks/task/add-task.html', dict(form=form))
