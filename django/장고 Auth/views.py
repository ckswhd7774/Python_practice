from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def index(request) :
    target_index = TodoList.objects.all()

    context = {'todos':target_index}
    return render(request, 'index.html', context)

def add(request) :

    if request.method == 'POST' :
        todo = request.POST['todo']

        add_todo = TodoList.objects.create(
            todo = todo
        )

        context = {'todo':add_todo}

        return redirect('index')

    return render(request, 'index.html')

def edit(request, pk) :
    target_edit = TodoList.objects.all()
    print(target_edit.first().todo)
    if request.method == 'POST' :
        todo = request.POST['edit']
        edit_todo = TodoList.objects.filter(pk=pk).update(
            todo =todo,
        )
        return redirect('index')

    context = {
        'pk':pk,
        'edits':target_edit
        }
    return render(request, 'edit.html', context)

def delete(request, delete_pk) :
    target_delete = get_object_or_404(TodoList, pk=delete_pk)

    Todo_pk = target_delete.pk

    target_delete.delete()

    return redirect('index')

def signup(request) :
    
    context = {
            'error' : {
                'state' : False,
                'msg' : '',
                'signup_msg' : ' '
            },
        }
        
    if request.method == 'POST' :
        userid = request.POST['userid']
        password = request.POST['password']
        password_check = request.POST['password_check']

        if (userid and password and password_check) :
            user = User.objects.filter(username=userid)

            if  len(user) == 0 : 

                if len(userid) >= 4 :

                    if (password == password_check) and len(password) >= 6 :
                        user = User.objects.create_user(
                            username = userid,
                            password = password,
                            )

                        auth.login(request, user)
                        return redirect('index')

                    else :
                        context = {
                            'error' : {
                            'state' : True ,
                            'msg' : '비밀번호를 확인해주세요.',
                            'signup_msg' : '비밀번호는 6자리 이상이어야 합니다.'
                            }
                        }
                        return render(request, 'signup.html', context)

                else :
                    context = {
                        'error' : {
                        'state' : True,
                        'msg' : ' ',
                        'signup_msg' : '아이디는 4자리 이상이어야 합니다.'
                    },
                }
                return render(request, 'signup.html', context)

            else :
                context = {
                    'error' : {
                    'state' : True,
                    'msg' : '이미 존재하는 아이디입니다.',
                    'signup_msg' : ' '
                    },
                }
                return render(request, 'signup.html', context)

        else : 
            context = {
                'error' : {
                'state' : True,
                'msg' : '모든 항목을 입력해주세요.',
                }
            }
            return render(request, 'signup.html', context)

    return render(request, 'signup.html', context)

def login(request) : 

    context = {
            'error' : {
                'state' : False,
                'msg' : '에러메시지',
            },
        }

    if request.method == 'POST' :
        login_id = request.POST['userid']
        login_pw = request.POST['password']
        
        user = User.objects.filter(username=login_id)
        
        if (login_id and login_pw) :

            if len(user) != 0 :

                user = auth.authenticate(
                    username = login_id,
                    password = login_pw
                )
                if user != None :
                    auth.login(request, user)

                    return redirect('index')

                else :
                    context['error']['state'] = True
                    context['error']['msg'] = '아이디 혹은 비밀번호를 확인해주세요'
                
            else :
                context['error']['state'] = True
                context['error']['msg'] = '존재하지 않는 아이디입니다.'

        else :
            context['error']['state'] = True
            context['error']['msg'] = '아이디와 비밀번호를 입력해주세요.'

    return render(request, 'login.html', context)

def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        
    return redirect('index')
