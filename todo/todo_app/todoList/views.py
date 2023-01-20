from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from todoList.serializers import ItemSerializers
from django.http import HttpResponseRedirect, JsonResponse


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.order_by('-created_at')


def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)

    return redirect('todoList:index')


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todoList:index')


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True

    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todoList:index')


def tasks_list(request):
    if request.method == 'GET':
        tasks = [
            Todo(
                user_name='Abc',
                title='Run',
                text='Running',
                datetime='10.01.23',
                done=True
            )
        ]
        return JsonResponse(ItemSerializers(tasks, many=True).data, safe=False)
