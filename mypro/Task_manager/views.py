from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import TaskEntry


def index(request):
    all_task_list = []
    task_list = TaskEntry.objects.filter(Task_dependant='None')

    for each_items in task_list:
        sub_task_list = TaskEntry.objects.filter(Task_dependant=each_items.Task_id)
        all_task_list.append({'main': each_items})
        if len(sub_task_list) > 0:
            for each in sub_task_list:
                all_task_list.append({'sub': each})

    print(all_task_list)

    for i in all_task_list:
        print(i)

    return render(request, 'index.html', context={'task_list': all_task_list})


def add(request):
    TaskEntryFormSet = modelformset_factory(TaskEntry, fields=(
    'Task_id', 'Task_des', 'Task_priority', 'Task_weight', 'Task_dependant', 'Task_schedule'), can_delete=True)

    if request.method == 'POST':
        formset = TaskEntryFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
        return HttpResponseRedirect("add")

    else:
        formset = TaskEntryFormSet()

    return render(request, 'add.html', {'formset': formset})


def edit(request):
    TaskEntryFormSet = modelformset_factory(TaskEntry, fields=(
    'Task_id', 'Task_des', 'Task_priority', 'Task_weight', 'Task_dependant', 'Task_schedule'))
    if request.method == 'POST':
        formset = TaskEntryFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = TaskEntryFormSet()
    return render(request, 'edit.html')
