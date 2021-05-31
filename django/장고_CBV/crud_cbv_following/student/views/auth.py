from django.http import request
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth

from social.services import ClassRoomService, Comment_Service
from student.services import CommentService, UserService, SignupDto, LoginDto, CommentDto

class SignupView(View) :
    def get(self, request, *args, **kwargs) :
        class_room_list = ClassRoomService.find_all()
        context = { 'class_room_list' : class_room_list}
        return render(request, 'signup.html', context)
        
    def post(self, request, *args, **kwargs) : 
        signup_dto = self._build_signup_dto(request.POST)
        result = UserService.signup(signup_dto)
        class_room_list = ClassRoomService.find_all()

        if (result['error']['state']) :
            context = { 'error' : result['error'], 'class_room_list': class_room_list }
            return render(request, 'signup.html', context)
        auth.login(request, result['user'])
        return redirect('social:class_list')

    @staticmethod
    def _build_signup_dto(post_data) :
        return SignupDto(
            userid=post_data['userid'],
            password=post_data['password'],
            class_room_pk=post_data['class_room_pk'],
            password_check=post_data['password_check'],
            introduce_text=post_data['introduce_text'],
            name=post_data['name'],
        )

class LoginView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs) :
        login_dto = self._build_login_dto(request.POST)
        result = UserService.login(login_dto)
        if (result['error']['state']) :
            context = { 'error' : result['error'] }
            return render(request, 'login.html', context)
        auth.login(request, result['user'])
        return redirect('social:class_list')

    @staticmethod
    def _build_login_dto(post_data) :
        return LoginDto(
            userid=post_data['userid'],
            password=post_data['password']
        )

def logout(request) :
    auth.logout(request)
    return redirect('index')