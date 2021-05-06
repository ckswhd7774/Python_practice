from django.contrib import admin
from django.urls import path
from Todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:delete_pk>', views.delete, name='delete'),
]
