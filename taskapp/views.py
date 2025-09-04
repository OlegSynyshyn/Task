from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Task, Comment
from django.urls import reverse_lazy

from taskapp.forms import TaskForm, TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_created.html'
    form_class = TaskForm
    success_url = reverse_lazy("task_create")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)