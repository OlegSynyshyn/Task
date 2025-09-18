from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "priority", "status", "deadline", "file"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields["deadline"].widget = forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control mb-2"}
        )
       
        for field_name, field in self.fields.items():
            if field_name != "deadline": 
                field.widget.attrs.update({"class": "form-control mb-2"})


class TaskFilterForm(forms.Form):
    PRIORITY_CHOICES = [
        ('', 'Усі'),
        ('Low', 'Низький пріоритет'),
        ('Medium', 'Середній пріоритет'),
        ('High', 'Високий пріоритет'),
    ]

    STATUS_CHOICES = [
        ('', 'Усі'),
        ('Pending', 'Потрібно виконати'),
        ('In_progres', 'У процесі'),
        ('Done', 'Виконано'),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, label='Пріоритет', required=False)
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Статус', required=False)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")