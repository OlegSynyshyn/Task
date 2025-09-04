from django import forms
from .models import Task # Припустимо, у вас є модель Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "priority", "status", "deadline", "file"] # Поля для форми

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["deadline"].widget = forms.DateTimeInput(attrs={"type": "Datetime-local"})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-2'})
            
        