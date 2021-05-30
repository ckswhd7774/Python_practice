from django.urls import path

from .views.auth import LoginView, SignupView, logout
from .views.crud import StudentDetailView, StudentEditView

app_name = 'student'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('signup/', SignupView.as_view(), name='signup'),
    
    path('logout/', logout, name='logout'),
    
    path('detail/<pk>', StudentDetailView.as_view(), name='detail'),
    path('edit/<pk>', StudentEditView.as_view(), name='edit'),
]