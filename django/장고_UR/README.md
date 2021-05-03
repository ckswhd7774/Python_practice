# 장고 UD 실습

Update /  Delete

### 업로드한 게시물을 볼 수 있는 디테일 페이지/ 수정, 삭제 기능

### 필요한 페이지

```python
1. index/     카테고리 나열
2. result/   각 카테고리의 게시물 나열
3. detail/   게시물 디테일 페이지
4. add/      게시물 추가 페이지
5. edit/     게시물 수정 페이지
```
<br>
### 기능 리스트업

```python
1. 각 게시물의 디테일 정보 보여주는 detail 페이지 만들기
2. 게시물 정보 수정할 수 있는 edit 페이지 만들기
3. edit 에서는 기존 값이 채워진 상태로 보여주기
4. edit 에서 업데이트 구현하기
5. delete 버튼을 누르면 정말 삭제할 것인지 한번 더 confirm 하기
6. delete 처리하기
7. delete 된 후에 해당 반으로 넘겨주기 
```
<br>
### models.py 에 데이터를 수정하기

```python
모델명.objects.filter().update()
```

update()함수는 queryset 에서만 적용되기 때문에, filter를 사용해야한다.
<br>
### models.py 에 데이터를 삭제하기

```python
모델명.objects.delete()
```
<br>
해당 모델의 필드명에 데이터를 추가해주면 된다.

### 수정하기 - urls.py

```python
path('detail/<int:detail_pk>', views.detail, name='detail')
path('edit/<int:edit_pk>', views.edit, name='edit')
```
<br>
### 수정하기 - views.py

```python
def edit(request, edit_pk) :
    
    article = get_object_or_404(Category, pk=edit_pk)
    if request.method == 'POST' :
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']
        
        category_edit = Category.objects.filter(pk=edit_pk).update(
            title=title,
            content=content,
            writer=writer,
        )

        return redirect('detail', edit_pk)
    
    context = {'article':article}
    return render(request, 'edit.html', context)
```

함수 edit 는 인자로 request 와 edit_pk를 받는다. edit_pk 는 urls.py에서 넘긴 pk 이다.

**get_object_or_404** 함수를 이용해 model에 있는 Category를 가져온다. (get 방식으로 데이터를 가져오면 try / except 를 꼭 사용해줘야 하는데  **get_object_or_404** 함수는 그 처리를 자동으로 해준다.)

그리고 POST를 이용해 각 인스턴스를 변수에 담고  모델명.objects.filter().update() 를 사용해 models.py의 데이터를 수정한다.
<br><br>
### 수정하기 - detail.html

```python
<ul>
	<h1>detail</h1>
    <li>{{detail.title}}</li>
    <li>{{detail.content}}</li>
    <li>{{detail.writer}}</li>
</ul>
<a href="{% url 'edit' detail.pk %}">수정하기</a>
```

수정하기 클릭 시 edit페이지로  url을 넘긴다.  이 때,  detail의 있는 데이터를 가지고 넘겨줘야 하므로 detail.pk를 같이 넘겨준다.

(왜냐하면 detail 페이지를 수정하려면 그 페이지의 데이터가 필요하기 때문이다.)
<br><br>
### 수정하기 - edit.html

```python
<h1>edit</h1>
    <form action="{% url 'edit' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="text"  name='title' placeholder="글의 제목" value="{{article.title}}"><br/><br/>
        <textarea name="content" placeholder="글의 내용">{{article.content}}</textarea><br/><br/>
        <input type="text" name="writer" placeholder="작성자" value="{{article.writer}}"><br/><br/>
        <button type="submit">수정하기</button>
    </form>
```
<br><br>
### 삭제하기 - result.html

```python
<form action="{% url 'delete' content.pk %}" method="POST">
	{% csrf_token %}
  <button type="submit" onclick="return confirm('정말 삭제하시겠습니다?');">삭제하기</button>
</form>
```

form 태그 action을 이용해서 delete로 넘긴다. (이 때 delete 페이지는 따로 없으며 views.py에 함수로만 존재한다.)

그리고 자바스크립트로  버튼 클릭 시 삭제할 것인지 확인해주는 이벤트를 걸어준다.
<br><br>
### 삭제하기 - urls.py

```python
path('delete/<int:delete_pk>', views.delete, name='delete')
```
<br>
### 삭제하기 - views.py

```python
def delete(request, delete_pk) :

    target_delete = get_object_or_404(Category, pk=delete_pk)
    
    delete_pk = target_delete.article.pk
    target_delete.delete()

    return redirect('result', delete_pk)
```

delete 함수도 마찬가지로 두번 째 인자로 delete_pk를 받는다.  

get_object_or_404()  함수의 첫 번째 인자인 Category는 related_name 이다.
<br><br>
## 1. index 페이지에 카테고리 나열
<img width="307" alt="스크린샷 2021-05-03 오후 2 09 59" src="https://user-images.githubusercontent.com/77820288/116843358-ac03f600-ac1a-11eb-9961-5f7b291c97f2.png">

<br><br>
## 2. 카테고리 클릭 시 해당 카테고리의 게시물들의 타이틀을 나열하는 result.html 로 이동
<img width="391" alt="스크린샷 2021-05-03 오후 2 10 21" src="https://user-images.githubusercontent.com/77820288/116843379-bfaf5c80-ac1a-11eb-857c-20cc26471f20.png">
<br><br>
## 3. 타이틀 클릭 시 세부 내용이 있는 detail.html 로 이동
<img width="387" alt="스크린샷 2021-05-03 오후 2 10 35" src="https://user-images.githubusercontent.com/77820288/116843391-c8a02e00-ac1a-11eb-8d0a-a3190e712d55.png">
<br><br>
## 4. 수정하기 클릭 시 세부 내용을 수정하는 edit.html로 이동 /수정완료 클릭 시 다시 detail.html 로 이동
<img width="390" alt="스크린샷 2021-05-03 오후 2 10 42" src="https://user-images.githubusercontent.com/77820288/116843406-d05fd280-ac1a-11eb-9640-5fecb22b05f1.png">
<br><br>
## 5. result 페이지에서 삭제하기 클릭 시 delete 된다.
<img width="701" alt="스크린샷 2021-05-03 오후 2 12 13" src="https://user-images.githubusercontent.com/77820288/116843425-d950a400-ac1a-11eb-9cc1-4586c85120b5.png">