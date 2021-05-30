from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from dataclasses import dataclass

from social.models import ClassRoom, Comment
from .models import Student

@dataclass
class SignupDto() :
    userid: str
    password: str
    password_check: str
    introduce_text: str
    name: str
    class_room_pk: str

@dataclass
class LoginDto() :
    userid: str
    password: str

@dataclass
class UpdateDto() :
    name: str
    introduce_text: str
    pk: str

@dataclass
class CommentDto() :
    content : str
    writer : User
    owner : User


ERROR_MSG = {
    'EXIST_ID' : '이미 존재하는 아이디 입니다.',
    'NO_EXIST_ID' : '존재하지 않는 아이디 입니다',
    'MISSING_INPUT' : '항목을 모두 채워주세요',
    'PASSWORD_CHECK' : '비밀번호를 확인해주세요',
}

def build_error_msg(msg_type):
    return {'error' : {'state' : True, 'msg' : ERROR_MSG['msg_type']}}

class UserService() :
    @staticmethod
    def find_by(user_pk) :
        return get_object_or_404(User, pk=user_pk)
    @staticmethod
    def find_by_class(class_pk) :
        return User.objects.filter(student__class_room__pk=class_pk)
    @staticmethod
    def signup(dto: SignupDto) : 
        if (not dto.class_room_pk or not dto.userid or not dto.password or not dto.password_check or not dto.introduce_text or not dto.name) :
            return build_error_msg('MISSING_INPUT')
        user = User.objects.filter(username=dto.userid)
        if (len(user) > 0) :
            return build_error_msg('EXIST_ID')
        if (dto.password != dto.password_check) :
            return build_error_msg('PASSWORD_CHECK')

        user = User.objects.create_user(username=dto.userid, password=dto.password)
        Student.objects.create(user=user, name=dto.name, introduce_text=dto.introduce_text, class_room=ClassRoom.objects.get(pk=dto.class_room_pk))

        return { 'error' : {'state' : False}, 'user' : user }

    @staticmethod
    def login(dto: LoginDto) :
        if (not dto.userid or not dto.password) :
            return { 'error' : {'state' : True, 'msg' : ERROR_MSG['MISSING_INPUT']} }
        user = User.objects.filter(username=dto.userid)
        if (len(user) == 0) :
            return { 'error' : {'state' : True, 'msg' : ERROR_MSG['NO_EXIST_ID']} }
        auth_user = authenticate(username=dto.userid, password=dto.password)

        return { 'error' : { 'state' : False }, 'user' : auth_user }

    @staticmethod
    def update(dto: UpdateDto) :
        if (not dto.name or not dto.introduce_text) :
            return { 'error' : {'state': True, 'msg' : ERROR_MSG['MISSING_INPUT']}}
        
        Student.objects.filter(pk=dto.pk).update(name=dto.name, introduce_text=dto.introduce_text)

        return { 'error' : { 'state' : False } }

class CommentService() :
    @staticmethod
    def comment(dto: CommentDto) :
        Comment.objects.create(
            content=dto.content,
            writer=dto.writer,
            owner=dto.owner
        )
