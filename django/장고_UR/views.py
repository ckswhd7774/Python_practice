from django.shortcuts import render, redirect, get_object_or_404
from .models import Home, Category
# Create your views here.

def index(request) :
    home_obj = Home.objects.all()
    category_obj = Category.objects.all()

    context = {'homes':home_obj,'categories':category_obj}
    return render(request, 'index.html', context)

def result(request, result_pk) :

    target_result = Home.objects.filter(pk=result_pk).first()

    return render(request, 'result.html',{'result':target_result})

def add(request, pk) :

    if request.method == 'POST' :
        article = Home.objects.filter(pk=pk).first()
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']

        category = Category.objects.create(
            article=article,
            title = title,
            content = content,
            writer=writer,
        )
        context = {'category':category}

        return redirect('add', category.pk)

    context = {'pk': pk}
    return render(request, 'add.html', context)

def detail(request, detail_pk) : 

    detail = get_object_or_404(Category, pk=detail_pk)
    context = {'detail':detail}
    return render(request, 'detail.html',context)

def edit(request, edit_pk) :
    
    article = get_object_or_404(Category, pk=edit_pk)
    if request.method == 'POST' :
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']
        
        category_edit = Category.objects.filter(pk=edit_pk).update(
            title=title,
            content=content,
            writer=writer,
        )

        return redirect('detail', edit_pk)
    
    context = {'article':article}
    return render(request, 'edit.html', context)

def delete(request, delete_pk) :

    target_delete = get_object_or_404(Category, pk=delete_pk)
    
    delete_pk = target_delete.article.pk
    target_delete.delete()

    return redirect('result', delete_pk)