from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('result/<int:result_pk>', views.result, name='result'),
    path('add/<int:pk>', views.add, name='add'),
    path('datail/<int:detail_pk>', views.detail, name='detail'),
    path('edit/<int:edit_pk>', views.edit, name='edit'),
    path('delete/<int:delete_pk>', views.delete, name='delete'),
]
