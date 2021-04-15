# while문

반목해서 문장을 수행해야 할 경우 while문을 사용한다.

## while문의 기본 구조

```python
while <조건문> : 
	<수행할 문장1>
	<수행할 문장1>
	<수행할 문장1>
	...
```

while문은 조건문이 참인 동안에 while문 아래의 문장을 반복해서 실행한다.

### while문 예시

```python
count = 0
while count < 10 :
	count += 1
	print(count)
	if count == 10 :
			print("반복문 종료")

//
1
2
3
4
5
6
7
8
9
10
반복문 종료
```

위 예제에서 count가 10보다 작은 동안에 while문을 계속 실행한다. count 가 10이 되면 조건문이 거짓이 되므로 while문을 빠져나가게 된다.

## while문 강제로 빠져나가기

while문은 조건문이 참인 동안 계속해서 반복적으로 실행한다. 하지만 강제로 빠져나가고 싶은 경우 break문을 사용한다.

```python
coffee = 10
money = 500
while money :
		print("돈은 받았으니 커피를 줍니다.")
		coffee -= 1
		print(f"남은 커피의 양은 {coffee}개 입니다")
		if coffee == 0:
				print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
				break
```

money는 500으로 고정되어있기 때문에 조건문인 money는 항상 참이다. 따라서 무한히 반복되는 무한 루프를 돌게 된다. 그리고 while문의 내용을 한 번 실행할 때마다 coffee의 개수는 1개씩 줄어든다. coffee가 0이 되면 "커피가 모두 소진되었습니다. 판매를 중지합니다." 문장이 실행되고 break문이 호출되어 while문을 빠져나가게 된다.

## while문의 맨 처음으로 돌아가기

while문 안의 문장을 실핼할 때 입력 조건을 검사해서 조건에 맞지 않으면 while문을 빠져나간다. 그런데 프로그래밍을 하다보면 while문을 빠져나가지 않고 while문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우가 생기게 된다. 이때 continue문을 사용한다.

### 예시

```python
a = 0
while a < 10 :
		a += 1
		if a % 2 == 0 : continue
		print(a)
1
3
5
7
9

```

위 예는 1부터 10까지의 숫자 중 홀수만 출력하는 예이다. a가 10보다 작은 동안 1씩 계속 증가한다. a가 1인 경우(홀수인 경우) 그대로 출력되지만 a가 2인 경우(짝수인 경우) continue문을 실행한다. continue문은 while문의 맨 처음(조건문 : a < 10)으로 돌아가게 하는 명령어이다. 따라서 a가 짝수이면 print(a)는 실행되지 않는다.