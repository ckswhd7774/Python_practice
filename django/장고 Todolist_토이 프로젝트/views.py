from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList

# Create your views here.

def index(request) :
    target_index = TodoList.objects.all()

    context = {'todos':target_index}
    return render(request, 'index.html', context)

def add(request) :

    if request.method == 'POST' :
        todo = request.POST['todo']

        add_todo = TodoList.objects.create(
            todo = todo
        )

        context = {'todo':add_todo}

        return redirect('index')

    return render(request, 'index.html')

def edit(request, pk) :
    target_edit = TodoList.objects.all()
    print(target_edit.first().todo)
    if request.method == 'POST' :
        print(request.POST)
        todo = request.POST['edit']
        edit_todo = TodoList.objects.filter(pk=pk).update(
            todo =todo,
        )
        return redirect('index')

    context = {
        'pk':pk,
        'edits':target_edit
        }
    return render(request, 'edit.html', context)

def delete(request, delete_pk) :
    target_delete = get_object_or_404(TodoList, pk=delete_pk)

    Todo_pk = target_delete.pk

    target_delete.delete()

    return redirect('index')