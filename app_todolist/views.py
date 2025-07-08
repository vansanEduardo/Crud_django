from django.shortcuts import render,redirect,get_object_or_404
from .models import Task

# Create your views here.
def create_task(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request,  'todolist.html', {'tasks': tasks})
    elif request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        task = Task(
            title=title,
            description=description
        )

        task.save()

        return redirect('create_task')
    
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('create_task')

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    title = request.POST.get('title')
    description = request.POST.get('description')

    task.title = title
    task.description = description
    task.save()
    return redirect('create_task')