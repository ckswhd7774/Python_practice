from django.contrib import admin
from django.urls import path, include

from social.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('social/', include('social.urls')),
    path('', IndexTemplateView.as_view(), name='index'),
]
