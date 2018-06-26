from django.db import models


# Create your models here.

class TaskEntry(models.Model):
    Task_id = models.CharField(max_length=30)
    Task_des = models.CharField(max_length=200)
    Task_priority = models.IntegerField(default=1)
    Task_weight = models.IntegerField(default=1)
    Task_dependant = models.CharField(default=None,max_length=30)
    Task_schedule = models.IntegerField(default=1)
