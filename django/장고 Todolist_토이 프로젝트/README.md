# 장고 Todolist -  토이프로젝트

## 배웠던 템플릿 문법 정리

```python
1. {{변수}}
2. {% if 조건 %} {% endif %}
3. {% for user in users %} {% endfor %}
4. {% url '네임' 인자 %}
```

### 장고에서 템플릿은 '레이아웃'의 역할이라는 것을 명심해야한다.

템플릿 문법으로 어느정도의 로직을 구현할 수도 있지만, 템플릿에서의 로직 사용은 최대한 자제해야한다.

### filters

장고의 변수 내용을 필터시켜서 화면에 보여줄 수 있다.

 <br>

```python
{{classes | length}}
```

템플릿 필터를 이용하면, 변수의 길이를 사용할 수 있다.
<br>
```python
{{class.teacher | lower}}
```

변수의 출력결과를 소문자로 변경 가능하다. 
<br><br>
### 템플릿 상속

<img width="304" alt="스크린샷 2021-05-04 오후 8 32 12" src="https://user-images.githubusercontent.com/77820288/117240303-7a359e00-ae6b-11eb-8cd1-8c211716f8be.png">



base에서 기본적인 html의 틀을 작성하고, index 와 detail 에서 base 를 상속해서 사용한다.

 <br>

```python
{{% block 이름 %}
{{% endblodck 이름 %
```

위와 같이 base에서 블록 구간을 만들 수 있다. 

endblock 에서 이름은 필수는 아니지만, 블록이 여러개가 생길 경우 가독성이 매우 떨어지므로 필수적으로 작성하는것이 좋다.

```python
{% extends "base.html" %}
```

위와 같이 base.html 을 작식 html 에서 상속 받아 사용할 수 있다. 
<br><br>
템플릿 상속 예 1

```python
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{% static 'base.css' %}"/>
    {% block head %}
    {% endblock head %}
    <title>Document</title>
</head>
<body>
    <h1>아래부터는 블록 컨텐츠가 온다</h1>
    {% block content %}
    {% endblock content %}
</body>
</html>
```
<br><br>
템플릿 상속 예 2

```python
{% extends "base.html" %}

{% block content %}
<h1>My Todolist</h1>
<form action="{% url 'add' %}" method="POST">
    {% csrf_token %}
    <input type="text" placeholder="오늘 할일" name='todo'>
    <button type="submit">추가하기</button>
</form>
{% for todo in todos %}
<p>{{todo}}</p>
<a href="{% url 'edit' todo.pk %}">수정하기</a>
<a href="{% url 'delete' todo.pk %}">완료</a>
{% endfor %}
{% endblock content %}
```
<br><br>
### include

반복되어 사용하는 템플릿을 만들어두고, include로 사용하기

include를 통해서 반복해서 사용되는 (ex : footer) 템플릿을 만들어두고, 필요한 페이지마다 include 해서 사용할 수 있다.

```python
{% include "footer.html" %}
```

base.html 에 만들어둬도 되지만, 코드를 분리하면 가독성이 올라간다!
<br><br>
# Todolist 만들기

- 할 일 작성하기
- 할 일 목록보기 / 수정하기
- 할 일 삭제하기(완료)
- 템플릿 상속을 활용할 것
<br>
## urls.py 작성

먼저 urls.py를 작성한다.

```python
from django.contrib import admin
from django.urls import path
from Todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:delete_pk>', views.delete, name='delete'),
]
<br>
```
메인 루트 페이지 → index.html

할 일 추가하는 페이지 → add.html

할 일 수정하는 페이지 → edit.html

할 일 삭제   → 삭제의 경우 페이지가 따로 필요하지 않다.
<br><br>
## 메인 페이지 - views.py

```python
def index(request) :
    target_index = TodoList.objects.all()

    context = {'todos':target_index}
    return render(request, 'index.html', context)
```
<br>
## 메인 페이지 - index.html

```python
{% extends "base.html" %}

{% block content %}
<h1>My Todolist</h1>
<form action="{% url 'add' %}" method="POST">
    {% csrf_token %}
    <input type="text" placeholder="오늘 할일" name='todo'>
    <button type="submit">추가하기</button>
</form>
{% for todo in todos %}
<p>{{todo}}</p>
<a href="{% url 'edit' todo.pk %}">수정하기</a>
<a href="{% url 'delete' todo.pk %}">완료</a>
{% endfor %}
{% endblock content %}
```

base.html 템플릿 상속을 활용하였다.

수정하기 클릭 시  todo.pk 를 가지고 edit 페이지로 이동한다.

(views.py 의 edit 함수를 호출하는데 edit 함수는 edit 페이지로 이동시키는 기능을 한다.)
<br>
완료 클릭 시 todo.pk 를 가지고 views.py 에 있는 delete 함수를 호출한다. 

<img width="318" alt="스크린샷 2021-05-06 오전 11 53 28" src="https://user-images.githubusercontent.com/77820288/117239839-79e8d300-ae6a-11eb-9141-89c0e0089fc0.png">
<br><br>
## 할 일 추가 페이지 - views.py

```python
def add(request) :

    if request.method == 'POST' :
        todo = request.POST['todo']

        add_todo = TodoList.objects.create(
            todo = todo
        )

        context = {'todo':add_todo}

        return redirect('index')

    return render(request, 'index.html')
```

index.html 의 form 태그에서 method 가 POST 인 상황에서 name 이 todo인 것을 가져와서 todo 에 할당한다. 

models 에 데이터를 추가하도록 한다. 그리고 데이터 추가가 완료되면 index 페이지로 이동한다.
<br>
추가하기 버튼 클릭 시 추가된다.

<img width="314" alt="스크린샷 2021-05-06 오전 11 54 09" src="https://user-images.githubusercontent.com/77820288/117239875-8a994900-ae6a-11eb-874d-e1c04a80ce55.png">

<br><br>
## 할 일 수정하기 - views.py

```python
def edit(request, pk) :
    target_edit = TodoList.objects.all()

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
```

models 에 저장되어 있는  데이터를 조회해서( 이 떄 그 해당 pk를 가지고 있는 데이터만 조회한다) 수정하도록 해준다. 이 때 수정하기 버튼을 누르면 edit.html 로 이동한다. 

수정이 완료되면 redirect 함수를 통해서 index 페이지로 이동한다.
<br>
## 할 일 수정하기 - edit.html

```python
{% extends "base.html" %}

{% block content %}
<h1>My Todolist</h1>
<form action="{% url 'add' %}" method="POST">
    {% csrf_token %}
    <input type="text" placeholder="오늘 할일" name='todo'>
    <button type="submit">추가하기</button>
</form>
{% for edit in edits %}
    {% if edit.pk == pk %}
<form action="{% url 'edit' edit.pk %}" method="POST">
    {% csrf_token %}
    <input type="text" value="{{edit}}" name='edit'>
   <button type="submit">수정하기</button>
</form>
    {% else %}
    <p>{{edit.todo}}</p>
    <a href="{% url 'edit' edit.pk %}">수정하기</a>
<a href="#">완료</a>
{% endif %}
{% endfor %}
{% endblock content %}
```
<br>
수정하기를 누르면 인풋태그로 바뀌며 수정이 가능하다.

<img width="339" alt="스크린샷 2021-05-06 오전 11 54 48" src="https://user-images.githubusercontent.com/77820288/117239898-96850b00-ae6a-11eb-9890-cf851d4ec182.png">
<br><br>
## 할 일 삭제하기 - views.py

```python
def delete(request, delete_pk) :
    target_delete = get_object_or_404(TodoList, pk=delete_pk)

    Todo_pk = target_delete.pk

    target_delete.delete()

    return redirect('index')
```

delete 함수를 이용해 모델에 저장되어 있는 데이터를 삭제할 수 있다. 
<br>
완료를 누르면 삭제된다.


<img width="310" alt="스크린샷 2021-05-06 오전 11 56 03" src="https://user-images.githubusercontent.com/77820288/117239915-a13fa000-ae6a-11eb-843d-2540e7e61287.png">
