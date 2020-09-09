from django.shortcuts import render, redirect

from tasks.forms import ContentForm
from tasks.models import TasksDB




def index(request):
    content = TasksDB.objects.all()
    context = {
        'tasks': content,
        'form': ContentForm()
    }
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'list.html', context)
    return render(request, 'list.html', context)


def index_delete(request, id):
    print(id)
    item = TasksDB.objects.get(id=id)
    item.delete()
    return redirect('/tasks')
