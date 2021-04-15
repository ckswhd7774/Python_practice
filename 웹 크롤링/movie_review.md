# 웹 스크래핑 2


이번엔 그 영화의 댓글을 가져오는 것을 목표로 스크래핑 하였다.

먼저 그 웹페이지의 url을 가져와야 하는데 내가 가져오려는 웹페이지는 iframe 으로 되어있어서 바로 가져올 수 없다.

그래서 다른 방식으로 가져와야한다.



<img width="1148" alt="스크린샷 2021-04-15 오후 3 33 41" src="https://user-images.githubusercontent.com/77820288/114829135-aaa69100-9e05-11eb-9c03-6c2d27e7559a.png">

이렇게 개발자 도구에서 network 탭에서 response를 얻어낸다. cURL을 복사한 뒤 


<img width="989" alt="스크린샷 2021-04-15 오후 3 36 58" src="https://user-images.githubusercontent.com/77820288/114829398-fbb68500-9e05-11eb-9391-fe72069467ef.png">


이 사이트에서 cURL을 Python request로 변환한다.

```python
import requests
from bs4 import BeautifulSoup

import requests

headers = {
    'authority': 'movie.naver.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189075',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=LSJFAQJ25JLGA; nx_ssl=2; BMR=s=1617886384522&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.nhn%3FblogId%3Dndb796%26logNo%3D221406934376%26proxyReferer%3Dhttps%3A%252F%252Fwww.google.com%252F&r2=https%3A%2F%2Fwww.google.com%2F; _ga=GA1.2.1862336832.1617084277; _ga_7VKFYR6RV1=GS1.1.1618365624.14.0.1618365624.60; page_uid=hciIWlprvTossf+91SCssssss4d-418800; NM_THUMB_PROMOTION_BLOCK=Y; csrf_token=173b0996-c924-4a7d-ac08-55d5f8e5b6ba',
}

params = (
    ('code', '189075'),
    ('type', 'after'),
    ('isActualPointWriteExecute', 'false'),
    ('isMileageSubscriptionAlready', 'false'),
    ('isMileageSubscriptionReject', 'false'),
)

response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
```

위 방식을 통해 URL을 가져왔다.



그 후 내가 가져오고 싶은 타겟에 접근해야 한다.

<img width="1053" alt="스크린샷 2021-04-15 오후 3 44 02" src="https://user-images.githubusercontent.com/77820288/114829442-0b35ce00-9e06-11eb-80f2-16093bd994dc.png">



댓글들은 ul 태그 안에 li 태그들로 이루어져 있으므로 select로 li 전체를 가져온다.

```python
review_list = soup.select('body > div > div > div.score_result > ul > li')
```



```python
review_list = soup.select('body > div > div > div.score_result > ul > li')
count = 0
for reviews in review_list :
  	review = reviews.select_one(f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()
    count += 1
    print(review)
```

자세히 보면 댓글들은 span 태그 안에 "_filtered_ment_숫자" 라는 id가 1씩 증가하면서 이루어져있다. 그래서 반복문을 통해 그 숫자를 1씩 증가시키면서 댓글들을 모두 가져온다.



하지만 여기서 간과한 것이 있다. 

<img width="907" alt="스크린샷 2021-04-15 오후 3 51 10" src="https://user-images.githubusercontent.com/77820288/114829490-1ab51700-9e06-11eb-9e45-500a89698a6d.png">


글자수 제한을 넘어가면 그 뒤는 출력이 안된다는 것이다. 저 댓글을 보면 span 태그 안에 또 span 태그가 있고 'data-src' 안에 텍스트가 담겨있다. 이 경우에는 예외처리를 해줘야 한다. 



```python
count = 0
for reviews in review_list :
    review = reviews.select_one(f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()
    if reviews.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span') :
        print(reviews.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span > a')['data-src'])
    else :
        print(review)
    count +=1
```

조건문을 사용해서 만약 span 태그 안에 span 태그가 존재할 경우 그 안의 텍스트를 가져오고 아니라면 review를 출력한다.



일단 1 페이지에 있는 댓글들은 모두 가져왔다. 총 10페이지의 댓글들 모두 가져오고 싶다면 어떻게 해야 할까?

<img width="904" alt="스크린샷 2021-04-15 오후 4 00 43" src="https://user-images.githubusercontent.com/77820288/114829553-2d2f5080-9e06-11eb-932c-e8f3ce0834ae.png">


보면 Query String Parameters 에서 page의 숫자가 페이지에 따라 바뀐다. 이 점을 이용해서 모든 페이지를 순회하면서 댓글들을 가져올 수 있다.



```python
for i in range(11) :
    params = (
    ('code', '189075'),
    ('type', 'after'),
    ('isActualPointWriteExecute', 'false'),
    ('isMileageSubscriptionAlready', 'false'),
    ('isMileageSubscriptionReject', 'false'),
    ('page', f'{i}'),)
    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
```

위 코드는 params 안의 page를 0부터 10까지 1씩 증가시킨다. 즉, 1페이지부터 10페이지까지 순회한다.

처음에는 reponse를 for문 밖에 두고 실행했는데 첫 번째 페이지의 댓글들만 10번 출력되는 것이었다. 왜그런가 보니 params의 바뀐 내용을 requests를 보내도 reponse는 변경되지 않는 내용만 주기 때문에 같은 페이지의 댓글들만 보내주는 것이었다.

그래서 response도 for문 안에 두어 바뀐내용을 즉각 받을 수 있도록 해야 한다.

**웹은 response와 requests로 이루어져있다.**



```python
import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'movie.naver.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189075',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=LSJFAQJ25JLGA; nx_ssl=2; BMR=s=1617886384522&r=https%3A%2F%2Fm.blog.naver.com%2FPostView.nhn%3FblogId%3Dndb796%26logNo%3D221406934376%26proxyReferer%3Dhttps%3A%252F%252Fwww.google.com%252F&r2=https%3A%2F%2Fwww.google.com%2F; _gid=GA1.2.329443640.1618316042; _ga=GA1.2.1862336832.1617084277; _ga_7VKFYR6RV1=GS1.1.1618365624.14.0.1618365624.60; page_uid=hciIWlprvTossf+91SCssssss4d-418800; NM_THUMB_PROMOTION_BLOCK=Y; csrf_token=be53d453-e3c8-47ac-be93-01293339fa6c',
}

params = (
    ('code', '189075'),
    ('type', 'after'),
    ('isActualPointWriteExecute', 'false'),
    ('isMileageSubscriptionAlready', 'false'),
    ('isMileageSubscriptionReject', 'false'),
    ('page', '1'),
)

def get_reviews(page_len):
    for i in range(page_len) :
        params = (
        ('code', '189075'),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
        ('page', f'{i}'),)
        response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        review_list = soup.select('body > div > div > div.score_result > ul > li')
        count = 0
        for reviews in review_list :
            review = reviews.select_one(f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()
            if reviews.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span') :
                print(reviews.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span > a')['data-src'])
            else :
                print(review)
            count +=1
    return review

get_reviews(11)
```

코드가 완성되면 함수 단위로 만들어 주는 것이 좋다. 사실 위의 함수는 여러개의 일을 하고 있기 때문에 좋은 코드는 아니다.

한개의 함수는 하나의 일을 하는 것이 좋다.

