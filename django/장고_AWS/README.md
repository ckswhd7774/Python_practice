# AWS란?

- 여러 클라우드 기반의 서비스를 제공

- 서비스 운영에 필수적인 파일 저장, 서버 세팅, 데이터 관리 등등

### IAM

- 리소스에 대한 접근 권한을 제어하는 서비스

- S#FullAccess 권한을 주는 IAM 생성(상황에 맞춰 FullAccess 가 아닌 권한을 주는 IAM을 생성해 권한 조정도 가능하다.)

### S3

- Simple Storage Service

- 클라우드 스토리지 제공 서비스(이미지, 로그, 정적파일 등을 손쉽게 저장 가능)

### django에서 파일을 S3로 업로드가 가능하다.

- 컴퓨터에서 이미지를 저장하는 방식은 컴퓨터 저장공간을 많이 쓸 수 밖에 없고, 여러 서버의 상테를 동일하게 유지하기 어렵다.

### S3에 이미지 저장 -> 장고에서 해당 url 저장

- 퍼블릭 엑세스를 전체 차단하고, cloudfront 등을 사용하는 것이 좋지만, 현재는 S3에서 read only 를 허용하는 방식으로 구현(권한에 대한 것은 굉장히 다양한 방법과 상황이 존재한다.)

### S3를 사용하기 전 준비사항

- pip install django-environ
- pip install boto3
- .env 에 secretkey 등을 저장하고 .gitignore 에 추가

### .env 에 secretkey 저장

```python
AWS_ACCESS_KEY_ID="입력 필요"
AWS_SECRET_ACCESS_KEY="입력 필요"
AWS_STORAGE_BUCKET_NAME="입력 필요"
```

### setting.py

- environ 패키지를 이용해 간편하게 env 읽어오기

```python
import environ

env = environ.Env()
environ.Env.read_env()
```

- 실제 파일 업로드 작업 시 사용하게 될 변수 작성

```python
# AWS

AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME='ap-northeast-2'
AWS_S3_OVERWRITE=False
```

### views.py

- 파일 업로드 시 사용하게 될 boto3 임포트

```python
from .models import Post
import boto3
from boto3.session import Session
from datetime import datetime
```

```python
def index(request) :
    if request.method == 'POST' :
        file = request.FILES.get('img')
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime('%Y%H%M%S')
        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key=now+file.name,
            Body=file
        )

        s3_url = 'https://django-s3-cj.s3.ap-northeast-2.amazonaws.com/'
        Post.objects.create(
            title=request.POST['title'],
            url = s3_url+now+file.name
        )
        return redirect('index')
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})
```

boto3 의 Session 함수를 이용해 각각의 Key를 담고 S3와 이어주는 로직을 작성한다.

그리고 s3_url 을 넣어주고 model 에 추가해준다.

### template

```python
{% for post in posts %}
        <img src="{{post.url }}" alt="{{post.title}}" width="400px;">
    {% endfor %}
    <form action="{% url 'index' %}" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <input type="file" name="img">
        <input type="text" name="title" placeholder="file name">
        <button type="submit">post</button>
    </form>
```

img 태그에 url을 넣어주면 이미지임을 인식한다.

### 

<img width="819" alt="스크린샷 2021-06-24 오후 6 15 24" src="https://user-images.githubusercontent.com/77820288/123237627-ca021e80-d518-11eb-8571-2d455707d36e.png">


### 

<img width="1116" alt="스크린샷 2021-06-24 오후 6 16 11" src="https://user-images.githubusercontent.com/77820288/123237670-d2f2f000-d518-11eb-9f9c-838cb177dc74.png">

이미지 업로드시 AWS 사이트의 S3에도 이미지가 저장이 되는 것을 볼 수 있다.