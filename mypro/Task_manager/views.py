from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import TaskEntry


def add(request):

    TaskEntryFormSet = modelformset_factory(TaskEntry, fields=(
    'Task_id', 'Task_des', 'Task_priority', 'Task_weight', 'Task_dependant', 'Task_schedule'),
                                            can_delete=True, error_messages="Error in submission")

    if request.method == 'POST':
        formset = TaskEntryFormSet(request.POST, request.FILES)

        if formset.is_valid():
            formset.save()

        return HttpResponseRedirect("add")
    else:
        formset = TaskEntryFormSet()

    return render(request, 'add.html', {'formset': formset})


def index(request):

    all_task_list = []
    task_list = TaskEntry.objects.exclude(Task_dependant__isnull=False)
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










# def add_a_task(request):
#
#     data = ''
#     if request.method == 'POST':
#         if request.POST['id']=='' or request.POST['des']=='' or request.POST['weight']=='' or request.POST['sw']==''  or request.POST['pri']=='':
#             data = "All fields are required"
#         else:
#             task = TaskEntry()
#             task.set_details(request.POST['id'],request.POST['des'],request.POST['pri'],request.POST['weight'],int(request.POST['dep']),request.POST['sw'])
#
#             print(request.POST['id'], request.POST['des'],request.POST['weight'], request.POST['sw'], request.POST['dep'] ,request.POST['pri'])
#
#     return render(request, 'addtask.html',context={'data':data})
