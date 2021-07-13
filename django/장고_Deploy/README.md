# django_Deploy

도커로 환경을 구축해두면 ec2 에서도 바로 배포가 가능하다.

여기선 git을 이용한 기본적인 배포로 진행하였다.

### docker-compose

도커 실행과 관련된 옵션들을 정리하고 간편히 실행.

컴포즈 파일은 yaml 을 이용하여 작성한다.

docker-compose란 이미지를 실행하는 설정을 담는다고 이해하면 된다. (여러 컨테이너를 사용할 경우 매우 유용하다.)

docker-compose 설치

```python
sudo curl -L https://github.com/docker/compose/releases/download/1.25.5/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose sudo chmod +x /usr/local/bin/docker-compose
```

### docker-compose.yml

```python
version: "3.7"
services:
  dev:
    container_name: dev
    build:
      context: .
      dockerfile: Dockerfile
		image: python-test
    env_file: .env
		ports: 
			- 9000:9000
    command: sh -c "python manage.py"
```

- version은 yml을 해석하기 위한 문법 버전이라고 보면 된다.(3 이상으로 맞춰서 사용하기)
- service는 생성할 컨테이너들이다.

service 아래로 컨테이너들의 목록이 온다고 생각하면 된다.(yml은 indent로 구분). service에서 들여쓰기 후 오는 이름이 하나의 서비스 명(컨테이너 명)이라고 생각하면 된다.

- build는 context에 build할 Dockerfile의 위치를 지정해주면 된다.

dockerfile에는 빌드할 Dockerfile의 이름이 다른 경우 지정해줄 수 있다.(Dockerfile 일 경우 생략도 가능하다.)

- env_file은 .env 파일을 불러올 수 있다.

.env 로 환경 변수를 관리중이라면 활용(Dockerfile에서 ENV로 관리해도 되지만 Dockerfile은 깃헙에 올리는 경우가 일반적이므로 .env로 관리해준다.)

- ports는 docker run 명령어의 -p 옵션이다. (포트 포워딩)
- command는 Dockerfile의 CMD와 같다고 생각하면 된다.

단, Dockerfile의 CMD도 존재할 경우에는 compose의 우선순위가 높다.

cf) sh -c : sh쉘로 실행한다는 의미이다.(docker에서 bash보다 범용적)

-c 옵션(뒤에 문자열로 명령어받기)

```python
docker-compose up [service 명]
```

yml 파일에 작성한 서비스(컨테이너)를 실행하는 명령어이다.(여러 옵션이 존재한다.)

ex) -build : 지정한 이미지를 빌드함, -d : 백그라운드 실행

docker-compose를 활용해 개발 환경과 프로덕션 환경을 구분해서 관리할 수 있다.(service로 필요한 설정등을 구분한다.)

## 개발 환경과 프로덕션 환경

개발하는 환경화 실제 서비스 환경은 차이가 존재한다.

### development

- [manage.py](http://manage.py) runserver로 실행
- 코드 변경시 자동으로 재실행 등등

### production

- [manage.py](http://manage.py) runserver로 실행 X
- 코드 변경 시 자동으로 재실행 필요 X

web server + web application server + django → 일반적인 프로덕션 세팅

### 웹서버 역할

웹서버(프록시 서버)를 이용하여 정적파일을 서빙.

- 웹서버를 사용하여 ddos 공격 등 보완적인 방어도 가능

정적 파일 서빙 + django로 오는 요청 WAS로 넘기기

### 웹 애플리케이션 서버(WAS) 역할

동적인 컨텐츠를 제공 + django로 요청 전달

여기서 웹서버는 nginx, WAS 역할로는 gunicorn을 사용할 것이다.

### nginx

대표적인 프록시 서버로 웹서버의 기능을 한다.

현재 가장 많이 사용하는 웹서버이기도 하다.

### gunicorn

WSGI로 웹서버와 어플리케이션간의 통신하기 위한 인터페이스

- WSGI는 파이썬 스크립트와 웹서버간의 미들웨어이다.

### docker-compose 장고 개발환경 세팅

```python
version: "3.7"
services:
  dev:
    container_name: dev
    build:
      context: .
      dockerfile: Dockerfile
    env_file: .env
    command: sh -c "python manage.py runserver 0:9000"
    volumes:
      - .:/django/
    ports:
      - "9000:9000"
```

volumes로 호스트의 소스코드 공유, .env.development로 연결하기

- .env를 프로덕션과 구분지어서 장고 세팅을 나눌 수 있게

### 프로덕션 세팅 - config/nginx/nginx.conf

```python
upstream production {
    ip_hash;
    server prod:8000;
}

server {
    server_name django.com;
    listen 80;
    location / {
        proxy_pass http://production/;
    }
    location /static/ {
        alias /static;
    }
}
```

### 프로덕션 세팅 - docker-compose nginx

```python
nginx:
    image: nginx:latest
    container_name: nginx_production
    ports:
      - "80:80"
    volumes:
      - .:/django
      - ./config/nginx/:/etc/nginx/conf.d
      - ./static:/static
    depends_on:
      - prod
```

### 프로덕션 세팅 - docker-compose prod

```python
prod:
    container_name: prod
    build:
      context: .
      dockerfile: Dockerfile
    env_file: .env
    command: sh -c "gunicorn config.wsgi:application --bind 0.0.0.0:8000"
    volumes:
      - .:/django/
    ports:
      - "8000:8000"
```

### 프로덕션 세팅 - config/settings

```python
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = ['0.0.0.0', 'production']
```

BASE_DIR의 parent 추가하기(settings 폴더 안이므로)

STATIC_ROOT 는 collectstatic 시 생기는 static 폴더 위치(nginx에서 서빙)

ALLOWE_HOST 미리 추가해주기

### 실행

```python
docker-compose up --build -d nginx
```

nginx의 depends on에 prod가 있기에 nginx만 up 해줘도 된다.

<img width="415" alt="스크린샷 2021-07-13 오후 1 25 44" src="https://user-images.githubusercontent.com/77820288/125391981-5305ca80-e3e0-11eb-8878-5cfa142ffd6c.png">


먼저 위의 과정을 거쳐 세팅해둔 파일들을 깃허브에 올린다. 그 후 깃 클론을 이용하여 AWS의 가상서버에 복사해온다.

<img width="1142" alt="스크린샷 2021-07-13 오후 1 29 14" src="https://user-images.githubusercontent.com/77820288/125392039-6c0e7b80-e3e0-11eb-9aa1-266cc1266da0.png">

```python
sudo docker-compose up
```

위의 명령어를 실행하면 AWS의 가상 서버를 통해 연결된 IP와 연동되어 성공적으로 배포가 되었다는 것을 알 수 있다.

(AWS → EC2에서 인스턴스 생성 후 가상 서버와 IP주소를 연동시킬 수 있다.)

<img width="416" alt="스크린샷 2021-07-13 오후 1 35 13" src="https://user-images.githubusercontent.com/77820288/125392070-7d578800-e3e0-11eb-83ce-4609db5151f2.png">