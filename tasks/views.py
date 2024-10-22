from django.db.models import F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddPostForm
from .models import Task


def task_list(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by('done', F('complete_before').asc(nulls_last=True))
    return render(request, 'tasks/task-list.html', dict(tasks=tasks))


def done_task(request: HttpRequest) -> HttpResponse:
    title = 'No complited tasks'
    tasks = Task.objects.filter(done=True)
    return render(request, 'tasks/task-list.html', dict(tasks=tasks, title=title))


def pending_task(request: HttpRequest) -> HttpResponse:
    title = 'No pending tasks'
    tasks = Task.objects.filter(done=False)
    return render(request, 'tasks/task-list.html', dict(tasks=tasks, title=title))


def task_detail(request: HttpRequest, task_slug: str) -> HttpResponse:
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task/task-detail.html', dict(task=task))


def add_task(request):
    if request.method == 'POST':
        if (form := AddPostForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = AddPostForm()
    return render(request, 'tasks/task/add-task.html', dict(form=form))


def edit_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'POST':
        if (form := AddPostForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = AddPostForm(instance=task)
    return render(request, 'tasks/task/edit-task.html', dict(form=form, task=task))


def delete_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.delete()
    return render(request, 'tasks/task/delete-task.html', dict(task=task))


def toggle_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    task.done = not task.done
    task.save()
    return redirect('tasks:task-list')
