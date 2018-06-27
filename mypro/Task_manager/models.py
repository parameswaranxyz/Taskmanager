from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import ModelForm


# Create your models here.

class TaskEntry(models.Model):
    Task_id = models.CharField(max_length=30)
    Task_des = models.CharField(max_length=200)
    Task_priority = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Task_weight = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Task_dependant = models.CharField(default='None',max_length=30)
    Task_schedule = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.Task_id

    def get_details(self):
        return [self.Task_id,self.Task_des,self.Task_priority,self.Task_weight,self.Task_dependant,self.Task_schedule]


class TaskForm(ModelForm):
    class Meta:
        model = TaskEntry
        fields = ['Task_id', 'Task_des', 'Task_priority','Task_weight','Task_dependant','Task_schedule']


