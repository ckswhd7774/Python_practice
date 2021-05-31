from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.http import request
from django.contrib.auth.models import User

from social.services import ClassRoomService, Comment_Service, LikeDto, LikeService, RelationshipDto, RelationSevice
from student.services import UserService, UpdateDto, CommentService, CommentDto
from student.models import Student, User

class StudentDetailView(generic.DetailView) :
    model = User
    context_object_name = 'user'
    template_name = 'detail.html'

class StudentEditView(View) :
    def get(self, request, *args, **kwargs) :
        context = { 'user' : UserService.find_by(kwargs['pk'])}
        return render(request, 'edit.html', context)

    def post(self, request, *args, **kwargs) :
        update_dto = self._build_update_dto(request.POST)
        result = UserService.update(update_dto) 
        if (result['error']['state']) :
            return render(request, 'edit.html')
        return redirect('student:detail', kwargs['pk'])

    def _build_update_dto(self, post_data) :
        return UpdateDto(
            name=post_data['name'],
            introduce_text=post_data['introduce_text'],
            pk=self.kwargs['pk']
        )

class CommentView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'student:detail.html')

    def post(self, request, *args, **kwargs) :
        comment_dto = self._build_comment_dto(request)
        CommentService.comment(comment_dto)
        print(kwargs['pk'])
        return redirect('student:detail',kwargs['pk'])

    def _build_comment_dto(self, request) :
        return CommentDto (
            content=request.POST['content'],
            writer=request.user,
            owner=User.objects.filter(pk=self.kwargs['pk']).first()
        )

class LikeView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'student:detail.html')

    def post(self, request, *args, **kwargs) :
        # 서비스로 넘기는 로직
        like_dto = self._build_like_dto(request)
        LikeService.toggle(like_dto)
        owner = LikeService.find_owner(kwargs['pk'])
        return redirect('student:detail', owner.pk)

    def _build_like_dto(self, request) :
        return LikeDto (
            comment_pk=self.kwargs['pk'],
            users=request.user
        )

class RelationshipView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'student:detail.html')

    def post(self, request, *args, **kwargs) :
        # 서비스로 넘기는 로직
        relationship_dto = self._build_relate_dto(request)
        result = RelationSevice.toggle(relationship_dto)
        return redirect('student:detail', kwargs['pk'])

    def _build_relate_dto(self, request) :
        return RelationshipDto(
            user_pk = self.kwargs['pk'],
            requester = request.user
        )