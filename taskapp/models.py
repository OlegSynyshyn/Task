from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Low", "Низький пріоритет"),
        ("Medium", "Середній пріоритет"),
        ("High", "Високий пріоритет")
    ]

    STATUS_CHOICES = [
        ("Pending", "Обов'язково"),
        ("In_progres", "В процесі"),
        ("Done", "Виконано")
    ]

    name = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, default="Low", verbose_name="Приорітет")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Low", verbose_name="Статус")
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="дедлайн")
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="користувач" )
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="сттворено в")
    file = models.FileField(upload_to="task_files/", null=True, blank=True, verbose_name="файл")

    def __str__(self):
        return f"{self.name} {self.status} {self.priority}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()
    file = models.FileField(upload_to="comment_files/", null=True, blank=True)
    def __str__(self):
        return f"{self.user} {self.task}"