from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('done/', views.done_task, name='done_task'),
    path('pending/', views.pending_task, name='pending_task'),
    path('t/<task_slug>/', views.task_detail, name='task-detail'),
    path('add-task/', views.add_task, name='add-task')
]
