# Django Authentication

## signup & login & logout

### Django의 내장 user로 authenticaiton 구현

기본적인 field를 제공하지만, 우리가 field를 추가하려면 custom 해야한다.
<br><br>
## 전체적인 흐름 - 회원가입

```python
1. POST 요청인지 확인
2. 제대로 input을 채워서 보냈는지 확인
3. 이미 사용중인 아이디인지 확인
4. 비밀번호 체크를 맞게 했는지 확인
5. 유저 모델 생성
6. 로그인 해주기
7. 리다이렉트 해주기
8. 회원가입 버튼 안보이게 하기
```

### 회원가입 - urls.py

```python
path('signup/', views.signup, name='signup'),
```
<br>
### 회원가입 - views.py

```python
from django.contrib.auth.models import User
from django.contrib import auth

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
```

context 형식을 미리 정의 해놓고 상태가 True가 되는 경우에만 에러 메시지를 띄우는 방향으로 정했다. 

먼저 장고의 user를 사용하기 위해선 장고 모델에서 user를 import 해줘야 한다. 

user라는 변수에 username과 password가 생성된 객체를 담고 그 객체를 이용해서 로그인해준다. 그 후에 redirect를 이용해 index로 돌아간다.

사실 위의 코드는 가독성이 심각하게 좋지않다. 그래서 로그인 함수는 더 간결한 방법으로 했다.
<br><br>
### 회원가입 - signup.html

```python
% extends "base.html" %}

{% block content %}
<h1>My Todolist</h1>
<h1>회원가입 페이지입니다.</h1>
{% if error.state %}
<h2>{{error.msg}}</h2>
<h2>{{error.signup_msg}}</h2>
{% endif %}
<form action="{% url 'signup' %}" method="POST">
    {% csrf_token %}
    <input type="text" placeholder="아이디" name="userid">
    <input type="password" placeholder="비밀번호" name="password">
    <input type="password" placeholder="비밀번호 확인" name="password_check">
    <button type="submit">회원가입</button>
</form>
{% endblock content %}
```

form 태그의 action 부분에서 url을 지정해주는 부분이 처음에는 버튼을 누르면 index로 가야되는게 맞지 않나?라는 생각이 들었다. 하지만 form 태그의 action은 해당 url로 이동하는 것이 아닌 아래 input 태그들의 정보를 해당 url로  전달하겠다라는 의미이다.
<br>
<img width="550" alt="스크린샷 2021-05-10 오후 8 11 26" src="https://user-images.githubusercontent.com/77820288/117651659-2a3d3b00-b1cd-11eb-8a86-d808e57f3b40.png">
<br>
<br>
<img width="548" alt="스크린샷 2021-05-10 오후 8 12 42" src="https://user-images.githubusercontent.com/77820288/117651714-3c1ede00-b1cd-11eb-9e55-e1936f49d7c5.png">


## 전체적인 흐름 - 로그인

```python
1. POST 요청인지 확인
2. 제대로 input을 채워서 보냈는지 확인
3. 존재하는 아이디인지 확인
4. 해당 아이디와 비밀번호가 맞는지 확인
5. 로그인 해주기
6. 리다이렉트 해주기
7. 로그인 버튼 안보이게 하기
8. 로그인 된 유저 이름 보여주기
```

### 로그인 - views.py

```python
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
```

위의 코드를 해석하자면 이렇다.

1 ) 만약 request.method가 POST라면 아래의 구문을 실행한다.

2 ) 만약  login_id 와 login_pw 가 참이라면 → 즉, 회원가입이 되어 있는 아이디라면 아래의 구문을 실행한다.

3 ) 만약 user의 길이가 0이 아니라면 → 즉,  존재하는 아이디라면 아래의 구문을 실행한다. 이 떄 auth.authenticate 함수를 이용하면 인증된 유저 아이디와 비밀번호가 담긴 객체를 변수 user 에 할당한다.

4 ) 만약 변수 user가 None이 아니라면 → 즉, 해당 아이디와 비밀번호가 맞다면 user 객체를 이용해 로그인하고 redirect를 이용해 index로 돌아간다. 

각각의 단계에서 if문을 통과하지 못한다면 설정되어 있는 에러 메시지가 뜨도록 하였다.
<br><br>
### 로그인 - login.html

```python
{% extends "base.html" %}

{% block content %}
<h1>My Todolist</h1>
<h1>로그인 페이지입니다.</h1>
{% if error.state %}
<h2>{{error.msg}}</h2>
{% endif %}
<form action="{% url 'login' %}" method="POST">
    {% csrf_token %}
    <input type="text" placeholder="아이디" name="userid">
    <input type="password" placeholder="비밀번호" name="password">
    <button type="submit">로그인</button>
</form>
{% endblock content %}
```

<img width="388" alt="스크린샷 2021-05-10 오후 8 12 53" src="https://user-images.githubusercontent.com/77820288/117651886-74beb780-b1cd-11eb-89fa-fbd528c99d1a.png">

<img width="396" alt="스크린샷 2021-05-10 오후 8 15 28" src="https://user-images.githubusercontent.com/77820288/117651908-7c7e5c00-b1cd-11eb-89d6-c156cb1acf2b.png">
<br><br>
### 메인 페이지 - index.html

```python
{% extends "base.html" %}

{% block content %}
<h1>My Todolist</h1>
<form action="{% url 'add' %}" method="POST">
    {% csrf_token %}
    <input type="text" placeholder="오늘 할일" name='todo'>
    <button type="submit">추가하기</button>
</form><br>
{% if user.is_authenticated %}
    <h1>{{user}}님 안녕하세요</h1><br>
    <form action="{% url 'logout' %}" method="POST">
        {% csrf_token %}
        <button type="submit">로그아웃</button>
    </form>
    {% for todo in todos %}
    <p>{{todo}}</p>
    <a href="{% url 'edit' todo.pk %}">수정하기</a>
    <a href="{% url 'delete' todo.pk %}">완료</a>
    {% endfor %}
{% else %}
<a href="{% url 'signup' %}">회원가입 </a><br><br>
<a href="{% url 'login' %}">로그인 하기</a>
{% endif %}
{% endblock content %}
```

만약 인증된 유저라면 유저 이름과 그 밖의 요소를 보여주고

로그인이 안되어있으면 회원가입과 로그인하기만 보여준다.
<br><br>
<img width="315" alt="스크린샷 2021-05-10 오후 8 13 28" src="https://user-images.githubusercontent.com/77820288/117651955-8acc7800-b1cd-11eb-88dc-c703677a6dda.png">

<img width="315" alt="스크린샷 2021-05-10 오후 8 11 11" src="https://user-images.githubusercontent.com/77820288/117651981-91f38600-b1cd-11eb-81a2-8bd205165155.png">

### 로그아웃 - views.py

```python
def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        
    return redirect('index')
```

로그아웃은 auth.logout 함수를 이용하면 간단하게 구현된다.