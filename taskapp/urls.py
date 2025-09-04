
from django.contrib import admin
from django.urls import path, include 
from taskapp import views
from .views import TaskListView, TaskCreateView




urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'), 
    path('create/', TaskCreateView.as_view(), name='task_create') 
]
