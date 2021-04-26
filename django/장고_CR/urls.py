from django.contrib import admin
from django.urls import path
from firstapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('category/<int:category_pk>', views.category, name='category'),
]