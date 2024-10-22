from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('done/', views.done_task, name='done-task'),
    path('pending/', views.pending_task, name='pending-task'),
    path('task/<task_slug>/', views.task_detail, name='task-detail'),
    path('add/', views.add_task, name='add-task'),
    path('task/<task_slug>/edit/', views.edit_task, name='edit-task'),
    path('task/<task_slug>/delete/', views.delete_task, name='delete-task'),
    path('task/<task_slug>/toggle/', views.toggle_task, name='toggle-task'),
]
