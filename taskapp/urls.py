from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('create/', views.TaskCreateView.as_view(), name='create_task'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='update_task'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete_task'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),


   
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
