from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import ModelForm


# Create your models here.

class TaskEntry(models.Model):
    Task_id = models.CharField(max_length=30,
                               error_messages={'incomplete': 'Enter a country calling code and a phone number.'},primary_key=True)
    Task_des = models.CharField(max_length=200)
    Task_priority = models.PositiveIntegerField(default=1,
                                                validators=[MinValueValidator(1), MaxValueValidator(5)],
                                                error_messages={
                                                    'incomplete': 'Enter a country calling code and a phone number.'})
    Task_weight = models.PositiveIntegerField(default=1,
                                              validators=[MinValueValidator(1), MaxValueValidator(5)])
    Task_dependant = models.ForeignKey('self',on_delete=models.CASCADE,blank=True, null=True)
    Task_schedule = models.PositiveIntegerField(default=1,
                                                validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.Task_id

    def get_details(self):
        return [self.Task_id, self.Task_des, self.Task_priority, self.Task_weight, self.Task_dependant,
                self.Task_schedule]

    def set_details(self, id, des, pri, wei, dep, sch):
        self.Task_id = id
        self.Task_des = des
        self.Task_priority = pri
        self.Task_weight = wei
        self.Task_dependant = dep
        self.Task_schedule = sch

        self.save()

        return True


class TaskForm(ModelForm):
    class Meta:
        model = TaskEntry
        fields = ['Task_id', 'Task_des', 'Task_priority', 'Task_weight', 'Task_dependant', 'Task_schedule']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False
