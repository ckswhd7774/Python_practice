from django.shortcuts import render
from .models import HomePage, Category
# from modele import 


# Create your views here.
def index(request) :
    homepage_object = HomePage.objects.all()
    category_object = Category.objects.all()

    context = {'homepages':homepage_object, 'categories':category_object}
    return render(request, 'index.html', context)

def category(request, category_pk) :
    target_category = HomePage.objects.filter(pk=category_pk).first()

    return render(request, 'category.html',{'category':target_category})