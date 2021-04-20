# 웹 스크래핑 3

### 네이버 금융 스크래핑

<img width="1152" alt="스크린샷 2021-04-20 오후 8 20 33" src="https://user-images.githubusercontent.com/77820288/115391366-5c84f980-a21a-11eb-8dc0-8a626f677590.png">


네이버 주식 페이지에서 순위별로 각각의 컨텐츠들을 뽑아오는 것을 목표로 스크래핑 하였다.

먼저 저번과 마찬가지로 이 웹페이지는 JS로 구성되어있기 때문에 개발자 도구 network 탭에서 이 페이지 접속할 때 받는 특정 response를 이용해서 cURL을 복사한다.

 그 후 [https://curl.trillworks.com/](https://curl.trillworks.com/) 에서 cURL을 Python requests로 변환해준다.

<img width="821" alt="스크린샷 2021-04-20 오후 8 14 11" src="https://user-images.githubusercontent.com/77820288/115391434-6eff3300-a21a-11eb-85cd-aa0bc8689ff1.png">


```python
import requests

headers = {
    'authority': 'finance.naver.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://finance.naver.com/',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=LSJFAQJ25JLGA; nx_ssl=2; nid_inf=790623602; NID_JKL=9jQVjZj97iA9uhmJwJxDaF5wcVK7uu/Sh9FrT215eVg=; _gid=GA1.2.517476890.1618804417; _ga=GA1.2.1862336832.1617084277; BMR=s=1618833242451&r=https%3A%2F%2Fseries.naver.com%2Fcomic%2Fdetail.nhn%3FproductNo%3D1844815&r2=https%3A%2F%2Fcomic.naver.com%2Fwebtoon%2Flist.nhn%3FtitleId%3D648419%26weekday%3Dmon; page_uid=hcHKJwp0J1sssaF7hX0ssssssnG-088880; _ga_7VKFYR6RV1=GS1.1.1618890046.18.0.1618890046.60; summary_item_type=recent; naver_stock_codeList=005930%7C035720%7C; JSESSIONID=099ED066AB5F141B69CB43A9C4A7B496',
}

response = requests.get('https://finance.naver.com/sise/lastsearch2.nhn', headers=headers)
```

cURL을 Python requests 로 변환하였다.

그 다음 뽑아오고 싶은 요소를 타겟팅한다.

<img width="498" alt="스크린샷 2021-04-20 오후 8 27 56" src="https://user-images.githubusercontent.com/77820288/115391481-7c1c2200-a21a-11eb-9cff-28b772572990.png">


순위 별 각 요소들은 tbody 태그 안에 tr 태그들로 이루어져 있다.

```python
tbody = soup.select('#contentarea > div.box_type_l > table > tbody')
```

tbody 태그 전체를 타겟팅하고 타겟팅이 잘 되었는지 확인해 보았다. 하지만 내가 기대한 값과는 달리 [], 빈 배열만 떴다. 한참을 찾다 원인을 알아냈다. 


<img width="1076" alt="스크린샷 2021-04-20 오후 8 34 54" src="https://user-images.githubusercontent.com/77820288/115391538-8a6a3e00-a21a-11eb-88af-054717bf1c28.png">



서버에서 받은 response에는 table 태그 안에 tbody가 없고 바로 tr 태그들이 있는것이었다. 

```python
tbody = soup.select('#contentarea > div.box_type_l > table > tr')
```

그리고 각 요소들은 tr 태그 안에 td 태그안에 있으므로 각각의 요소들을 변수로 지정한 후 반복문을 이용하여 차례대로 값을 뽑아왔다.

```python
for i in tbody :
		rank = i.select_one('td.no')
		title = i.select_one('td > a')
		search_percentage = i.select_one('tr > td:nth-child(3)')
		price = i.select_one('tr > td:nth-child(4)')
		rate_of_fluctuation = i.select_one('tr> td:nth-child(6) > span')
		transaction_volume = i.select_one('tr> td:nth-child(7)')
```

그리고 중간 확인을 해봤더니 이번엔 중간중간 None이 많이 나오는것을 확인하였다. 그 이유를 살펴보니 중간중간 텍스트 없는 태그들이 존재했기 때문이다. 비어있는 태그들을 예외처리하기 위해 조건문을 사용하였다.

```python
if title or rank or search_percentage or price: 
        print('순위', rank.text)
        print('종목명', title.text.strip())
        print('검색비율', search_percentage.text)
        print('현재가', price.text)
        print('등략률', rate_of_fluctuation.text.strip())
        print('거래량', transaction_volume.text)
        print('')
```

위의 방법들을 거쳐 내가 원하던 값들을 가져올 수 있었다.

```python
import request
from bs4 import BeautifulSoup

headers = {
    'authority': 'finance.naver.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://finance.naver.com/',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=LSJFAQJ25JLGA; nx_ssl=2; nid_inf=790623602; NID_JKL=9jQVjZj97iA9uhmJwJxDaF5wcVK7uu/Sh9FrT215eVg=; _gid=GA1.2.517476890.1618804417; _ga=GA1.2.1862336832.1617084277; BMR=s=1618833242451&r=https%3A%2F%2Fseries.naver.com%2Fcomic%2Fdetail.nhn%3FproductNo%3D1844815&r2=https%3A%2F%2Fcomic.naver.com%2Fwebtoon%2Flist.nhn%3FtitleId%3D648419%26weekday%3Dmon; page_uid=hcHKJwp0J1sssaF7hX0ssssssnG-088880; _ga_7VKFYR6RV1=GS1.1.1618890046.18.0.1618890046.60; summary_item_type=recent; naver_stock_codeList=005930%7C035720%7C; JSESSIONID=099ED066AB5F141B69CB43A9C4A7B496',
}

response = requests.get('https://finance.naver.com/sise/lastsearch2.nhn', headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
tbody = soup.select('#contentarea > div.box_type_l > table > tr')
data = []

for i in tbody :
    rank = i.select_one('td.no')
    title = i.select_one('td > a')
    search_percentage = i.select_one('tr > td:nth-child(3)')
    price = i.select_one('tr > td:nth-child(4)')
    rate_of_fluctuation = i.select_one('tr> td:nth-child(6) > span')
    transaction_volume = i.select_one('tr> td:nth-child(7)')
    if title or rank or search_percentage or price: 
        print('순위', rank.text)
        print('종목명', title.text.strip())
        print('검색비율', search_percentage.text)
        print('현재가', price.text)
        print('등략률', rate_of_fluctuation.text.strip())
        print('거래량', transaction_volume.text)
        print('')
        all_list = { 
        '순위': rank.text,
        '종목명': title.text.strip(),
        '검색비율': search_percentage.text,
        '현재가': price.text,
        '등략률': rate_of_fluctuation.text.strip(),
        '거래량': transaction_volume.text,
    }
        data.append(all_list)
print(data)
```

만들어진 값들을 딕셔너리로 만든 후 빈 리스트에  저장하였다. 그리고 csv 를 이용해 stock.csv 파일을 생성 후 그 파일에 데이터들을 저장하였다. 

```python
import csv 

with open('stock.csv', 'w', newline='') as csvfile :
    fieldnames = ['순위', '종목명', '검색비율', '현재가', '등략률', '거래량']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for all_data in data :
        writer.writerow(all_data)
```

<img width="638" alt="스크린샷 2021-04-20 오후 8 49 55" src="https://user-images.githubusercontent.com/77820288/115391585-981fc380-a21a-11eb-8ff7-108e33bdff5d.png">
