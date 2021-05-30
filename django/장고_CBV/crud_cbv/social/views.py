from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from social.models import ClassRoom
from student.services import UserService


class IndexTemplateView(generic.TemplateView) :
    template_name = 'index.html'

class ClassListView(LoginRequiredMixin, generic.ListView) :
    login_url = '/student/login/'
    redirect_field_name = None
    
    model = ClassRoom
    context_object_name = 'class_room_list'
    template_name = 'class-list.html'

class ClassDetailView(generic.DetailView) : 
    model = ClassRoom
    context_object_name = 'class_room'
    template_name = 'class.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['user_list'] = UserService.find_by_class(self.kwargs['pk'])
        return context

