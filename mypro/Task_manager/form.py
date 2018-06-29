from django.forms import ModelForm
from Task_manager.models import TaskEntry


class TaskForm(ModelForm):
    class Meta:
        model = TaskEntry
        fields = ['Task_id', 'Task_des', 'Task_priority', 'Task_weight', 'Task_dependant', 'Task_schedule']
