# **웹 스크래핑하기**

<img width="1030" alt="스크린샷 2021-04-14 오후 7 15 41" src="https://user-images.githubusercontent.com/77820288/114800890-8cc13800-9dd5-11eb-9bc7-9583a9ec3322.png">

네이버 영화 사이트에 접속하여 영화의 제목들을 뽑아오는 것을 목표로 스크래핑을 하였다.

먼저  virtualenv 가상환경에서 request 와 BeatufulSoup 모듈을 설치한 후  진행하였다.

```python
import requests
from bs4 import BeautifulSoup

# response에 requests로 얻은 URL을 할당한다.
response = requests.get('https://movie.naver.com/movie/running/current.nhn#')
# soup에 BeautifulSoup모듈을 사용하여 URL을 텍스트로 변환하고 파싱한다.
soup = BeauifulSoup(response.text, 'html.parser)
```

<img width="891" alt="스크린샷 2021-04-14 오후 7 26 50" src="https://user-images.githubusercontent.com/77820288/114800921-a19dcb80-9dd5-11eb-8ae6-68c761665154.png">

내가 스크랩하고 싶은 타겟이 HTML 구조 안에 어디에 위치해 있는지 확인한다.

그 다음 li_list 에 soup.select를 이용하여 내가 뽑고싶은 그 타겟을 할당한다. 

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(response.text, 'html.parser')

# 영화 페이지 전체
# 전체 ul 태그안에 한 영화씩 li태그들로 이루어져있다.
li_list = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
```

```python
# li_list에는 ul의 li들이 담겨있다. 그래서 반복문을 사용하여 li들을 모두 출력해야한다.
# dl 태그 안의 dt 태그 안의 a 태그안의 텍스트를 하나씩 가져온다.
title = title.select_one('dl > dt > a').text

# 위와 마친가지로 영화마다 고유의 값을 가져온다. 
href = title.select_one('dl > dt > a')['href']
```

여기서 주의할 점은 중간마다 내가 타겟을 제대로 가져왔는지 출력하면서 차근차근 하는것이 중요하다.

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://movie.naver.com/movie/running/current.nhn#')
soup = BeautifulSoup(response.text, 'html.parser')

# 영화 페이지 전체
li_list = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
for title in li_list :
    href = title.select_one('dl > dt > a')['href']
    title = title.select_one('dl > dt > a').text
    print(title)
    print(href.split('?code=')[1])
# for문을 사용하여 영화의 제목들과 고유한 코드를 순회하며 출력한다.
```

위 방법을 통해 한 페이지 안에 있는 영화의 제목들과 코드를 스크래핑할 수 있다.