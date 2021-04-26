# CR of python django

Create & Read

## foreign key로 연결된 데이터베이스 만들기

데이터베이스 테이블은 이런식으로 구성되어 있다.


<img width="383" alt="스크린샷 2021-04-26 오후 5 07 16" src="https://user-images.githubusercontent.com/77820288/116058360-b96d2d80-a6ba-11eb-99e0-e867112174a5.png">


foreign key로 다른 테이블을 가리킨다.

<img width="493" alt="스크린샷 2021-04-26 오후 5 08 49" src="https://user-images.githubusercontent.com/77820288/116058389-c1c56880-a6ba-11eb-92a8-e2ed08d5bbe7.png">


### 장고 준비

```python
1. mkdir 폴더명
2. cd 폴더명
3. virtualenv venv & source venv/bin/ activate (가상환경 설치 및 진입)
4. pip install django
5. django-admin startproject config .
6. python manage.py startapp 앱명
7. setting.py에 app 추가하기
```

### 먼저 model.py를 작성한다.

```python
from django.db import models

# Create your models here.

class Home(models.Model) :
    category_name = models.CharField(max_length=30)

    def __str__(self) :
        return self.category_name

class Category(models.Model) :
		article = models.ForeignKey('Home', on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)

    def __str__(self) :
        return self.title
```

위의 ForeignKey를 통해서 article과 Home이 연결되었다.

ForeignKey('어떤 클래스를 가리킬 것인가', Home 클리스에서 데이터가 삭제되면 나도 삭제하겠다, Home에서 Category 테이블을 뭐라고 부를것인가 (1:N 관계에서 나를 뭐라고 부를것인가))

## makemigrations

makemigrations를 통해서 모델의 정보를 기반으로 migrations를 생성한다. 

이 명령어를 통해서 방금 만든 모델이 적용된다. 모델이 변화가 있을 때 실행해주어야 하는 명령

## migrate 으로 실제 테이블 생성

migrate 명령얼르 통해서 실제로 migrations를 적용한다.

### 장고 admin을 이용하는 방법을 통해 데이터가 잘 생성되었는지 확인해볼 수 있다.

장고 admin이란 장고의 관리자 기능이다. 장고는 자체 admin을 제공해준다.

```python
python manage.py createsuperuser
```

관리자 계정을 생성하는 명령어

### 이전에 만든 model을 admin.py에 등록해야한다.

```python
admin.py

from django.contrib import admin
from .models import Home, Category

admin.site.register(Home)
admin.site.register(Category)
```

### views.py에서 생성한 models.py데이터를 가져오는 세가지 방법이 있다(조회).

1. models.objects.all()

    해당 모델에 저장된 모든 데이터를 조회하는 함수. 각각의 객체를 리턴한다.

2. models.objects.get(pk=1)

    특정 데이터만 조회하는 함수 : 유일한 값. pk로의 조회는 get을 활용하자.

3. models.objects.filter(class_num=2)

    특정 데이터만 조회하는 함수 : 여러 개

### views.py에서 models에 접근하기

```python
views.py

from django.shortcuts import render
from .models import Home, Category

def index(request) :
    home_obj = Home.objects.all()
    category_obj = Category.objects.all()

    context = {'homes':home_obj,'categories':category_obj}
    return render(request, 'index.html', context)

def result(request) :

    return render(request, 'result.html')
```

### 이제 urls.py에서 result.html의 데이터를 추가해준다.

```python
urls.py

from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('result/', views.result, name='result')
]
```

### index.html에서 반복문을 이용해 나열한다. 이 때 각 카테고리에 링크를 걸어서 그 링크를 클릭하면 해당 게시판으로 이동하게끔 해준다.

```python
index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>index</h1>
    <ul>
        {% for home in homes %}
        <li>
            <a href="{% url 'result' home.pk %}">{{home}}</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

각 카테고리를 클릭하면 result.html로 연결되는데 result로 연결할 때 pk 값을 보낸다.

### 루트에서 카테고리를 클릭해서 result로 넘어가는 기능 - urls.py

```python
urls.py

path('result/<int:result_pk>', views.result, name='result')
```

### 루트에서 카테고리를 클릭해서 result로 넘어가느 기능 - views.py

```python
views.py

def result(request, result_pk) :
    target_result = Home.objects.filter(pk=result_pk).first()

    return render(request, 'result.html',{'result':target_result})
```

result.html 로 넘길 때 클릭한 카테고리 정보를 모델로부터 가져와서 넘긴다.

result에서 각 카테고리의 게시물을 나열하는 기능 - result.html

```python
result.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>
        {% for content in result.article.all%}
            <li>title : {{content.title}}</li>
            <li>content : {{content.content}}</li>
            <li>writer : {{content.writer}}</li>
        {% endfor %}
    </h2>
</body>
</html>
```

<img width="396" alt="스크린샷 2021-04-26 오후 6 01 32" src="https://user-images.githubusercontent.com/77820288/116058429-cdb12a80-a6ba-11eb-88cc-a8fcd2d20cfc.png">


각 카테고리를 클릭하면 해당 카테고리의 게시판으로 이동한다.

<img width="393" alt="스크린샷 2021-04-26 오후 6 02 04" src="https://user-images.githubusercontent.com/77820288/116058465-d73a9280-a6ba-11eb-88a6-a0d73594d907.png">


<img width="397" alt="스크린샷 2021-04-26 오후 6 02 18" src="https://user-images.githubusercontent.com/77820288/116058508-e28dbe00-a6ba-11eb-942c-13ff3dee375c.png">
