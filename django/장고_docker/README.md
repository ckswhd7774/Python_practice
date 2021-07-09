# django_Docker

배포를 하기 위해 먼저 도커의 개념을 알고 있어야 한다.

### 도커란?

- 컨테이너를 기반한 가상화 플랫폼이다.
<br>
### 컨테이너란?

- 격리된 프로세스라고 이해할 수 있다.
- 시스템으로부터 프로세스를 격리해 독립된 환경을 만든 것(가상화)
<br>
## 컨테이너 VS VM
<br>
### VM

- 자체 OS를 포함 → 하드웨어 리소스를 많이 잡아먹는다.
- 물리적 하드웨어 계층에서 hypervisor를 통해 가상머신의 리소르를 분리한다. (하이퍼바이저란 VM을 구동하는 소프트웨어이다.)
<br>
### 컨테이너

컨테이너는 운영체제 수준에서 가상화 → 격리된 환경에서 프로세스로 돌아간다. 
<br>
### 도커의 장점

이미지를 구축해두고 이를 어디에서나 사용할 수 있다.

서버 환경에 맞춰 매번 세팅하는 것이 아닌, 어떠한 환경에서도 돌아가는 서버세팅을 가능하게한다. 

스케일 아웃 등의 상황에서도 손쉽게 대처가 가능하다.
<br>
### 이미지

이미지란 애플리케이션을 실행하기 위한 환경을 의미한다.

18.04 LTS 버전의 우분투를 사용하고, 3.7 버전의 파이썬을 사용하며 등등..의 환경들의 정적인 상태를 나타낸다.

<img width="291" alt="스크린샷 2021-07-08 오후 8 49 20" src="https://user-images.githubusercontent.com/77820288/125027712-a1098e00-e0c1-11eb-9b1f-a7cd473206c5.png">


도커의 이미지는 여러개의 레이어로 구성된다.

레이어 개념을 활용하여 효율적인 관리가 가능하다.
<br>
### 컨테이너

컨테이너란 이미지를 실행한 하나의 독립된 프로세스를 의미한다.

이미지로  만들어진 파일들(레이어)의 집합을 실행한것이 컨테이너이다.

이미지는 파일(레이어)들의 집합, 컨테이너는 이미지를 실행한 프로세스

공식 홈페이지에서 도커 설치가 가능하다.

<img width="464" alt="스크린샷 2021-07-09 오후 1 28 05" src="https://user-images.githubusercontent.com/77820288/125027732-ac5cb980-e0c1-11eb-803d-d12437ea63ee.png">

```python
docker images
```

호스트 컴퓨터에 pull 받은 image 목록을 볼 수 있다. (docker image ls와 같다.)
<br>

```python

docker pull centos
```

특정 os 이미지를 설치하는 과정이 매우 간편하다.

docker는 이미지를 다운 받고, 업로드하는 과정을 pull 과 push 로 표현한다.

도커에서는 이미지:<tag>로 버전을 구분한다.

따로 적지 않으면 latest 이미지를 pull 한다.<br>

```python
docker run -it <이미지명> <명령어>

// 이미지를 컨테이너로 실행하는 명령어
```

ex ) docker run -it centos bash

-i : 컨테이너와 상호작용을 하겠다.

-t : 터미널을 사용하겠다.

-d : 백그라운드로 실행하겠다.
<br>

<img width="491" alt="스크린샷 2021-07-09 오후 1 28 55" src="https://user-images.githubusercontent.com/77820288/125027746-b383c780-e0c1-11eb-818d-69522c2ab694.png">

위 이미지를 보면 현재 해당 도커의 컨테이너를 실행하고 있다.

```python
docker ps
```

—all 옵션으로 실행 할 경우 run 으로 실행 후 종료된 컨테이너까지 볼 수 있다.

(종료된 ps 를 docker restart <id>로 재실행이 가능하다.)<br>

<img width="564" alt="스크린샷 2021-07-09 오후 1 30 56" src="https://user-images.githubusercontent.com/77820288/125027988-3016a600-e0c2-11eb-8e63-a4995899f5b5.png">

```python
docker stop <container_id> / docker rm <contatiner_id>
```

container 를 중지하고 지울 수 있다.

```python
docker exex -it <container_id> <명령어>
```

docker run 과는 다르게 현재 실행중인 컨테이너 명령어를 전달 가능하다.<br>

### Dockerfile

Dockerfile이란 이미지를 만들기 위한 설정 파일이다.

다른 방법으로는 commit을 통해서 하나하나 할 수도 있지만 많이 사용하는 방법은 아니다.

Dockerfile 을 이용하여 간편하게 어떠한 환경을 세팅할지를 작성할 수 있다.

```python
FROM python:3.8

ENV PYTHONDONTWRITEBYCODE=1 \ 
		PYTHONUNBUFFERED=1

COPY ../app/
WORKDIR app/
RUN pip install request

CMD ["python", "test.py"]
```
<br>
- FROM은 해당 이미지를 pull하겠다이다. 도커 레포지토리에서 해당하는 이미지를 pull → dockrt pull 과 같은 의미이다.
- ENV 는 환경 변수를 설정할 수 있다. key=value 방식으로 여러 환경 변수를 하나의 명령어에 쓰는 것이 좋다.
- COPY는 컨테이너로 현재 호스트의 파일을 복살할 때 사용한다. ex ) COPY . ./app 은 현재 디렉토리(.)를 컨테이너릐 ./app 으로 복사하겠다는 명령어이다.
- WORKDIR 은 작업 할 디렉토리를 지정한다. cd 와 비슷하다고 생각하면 된다.
- RUN 명령 한 줄은 하나의 이미지 레이어를 만든다. 그러므로 되도록이면 한 줄에 작성하는것이 좋다. 패키지나 디펜던시 설치에 주로 사용한다.
- CMD 는 이미지를 모두 만들고 컨테이너로 실행하는 명령어이다. docker run 등의 마지막 인자로 넘기는 명령어라고 생각하면 된다.

```python
docker build -t test:latest
```

현재 위치에 있는 Dockerfile을 빌드하여 이미지를 만들고, latest 로 태그하는 명령어이다.<br>

```python
docker run test:latest
```

만든 이미지를 컨테이너로 실행하는 명령어이다.

그래서 Dockerfile을 이용하면 각 명령어들이 하나의 레이어를 만들어서 최종 이미지를 만드는 방식이다.

명령어를 한 줄에 작성 할 경우 효율적으로 작업 가능하다.<br>

```python
FROM python:3.8

ENV PYTHONDONTWRITEBYCODE=1 \
		PYTHONUNBUFFERED=1

RUN mkdir /django
WORKDIR /django

COPY requirements.txt /django/

RUN pip install --no-compile --no-cache-dir --upgrade pip && \ 
    pip install --no-compile --no-cache-dir -r requirements.txt

COPY . /django/
CMD ["./manage.py", "runserver", "0:8000"]
```

```python
docker run -p 8000:8000 <image>
```

-p 옵션을 줘서 컨테이너의 포트와 호스트의 포트를 포워딩 해줘야한다.