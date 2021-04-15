# for문

파이썬의 직관적인 특징을 가장 잘 대변해 주는 것이 바로 이 for문이다. while문과 비슷한 반복문인 for문은 매우 유용하고 문장 구조가 한눈에 들어온다.

## for문의 기본 구조

```python
for 변수 in 리스트(또는 튜플, 문자열) :
		수행할 문장1
		수행할 문장2
```

리스트나 튜플, 문자열의 첫 번째 요소이자 마지막 요소까지 차례로 변수에 대입되어 "수행할 문장1", "수행할 문장2"등이 실행된다.

### 전형적인 for문

```python
test_list = ['one', 'two', 'three']
for i in test_list :
		print(i)

// -> 
one
two
three
```

['one', 'two', 'three'] 리스트에 첫 번째 요소인 'one'이 먼저 변수 i에 대입된 후 print(i) 문장을 실행한다. 다음에 두 번째 요소'two'가 변수 i에 대입된 후 print(i) 문장을 실행하고 리스트의 마지막 요소까지 이것을 반복한다.

### 다양한 for문의 사용

```python
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a :
		print(first + last)
// ->
3
7
11
```

위 예는 a 리스트의 요소값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last) 변수에 대입된다.

### for문의 응용

```python
"총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고
그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오."
```

```python
scores = [90, 25, 67, 45, 80]

count = 0
for score in scores : 
		count =+ 1
		if score >= 60 :
				print(f"{count}번 학생은 합격입니다.")
		else : 
				print(f"{count}번 학생은 불합격입니다.")
// -> 
1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.
```

## for문과 continue

while문과 마친가지로 for문에서도 continu문을 사용할 수 있다. 

"60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무 메시지도 보내지 않는 반복문을 완성하시오."

```python
scores = [90, 25, 67, 45, 80]

count = 0
for score in scores :
		count =+ 1
		if score < 60:
				continue
		print(f'{count}번 학생 합격입니다. 축하합니다')
//->
1번 학생 축하합니다. 합격입니다.
3번 학생 축하합니다. 합격입니다.
5번 학생 축하합니다. 합격입니다.
```

## for문과 함께 자주 사용하는 range 함수

for문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다.

```python
a = range(10)
a
// -> range(0,10)
# 0부터 9까지
```

range(10)은 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다.

시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자) 형태를 사용하는데, 이 때 끝 숫자는 포함되지 않는다.

### 예시

```python
count = 0
for i in range(1, 11) :
		count =+ i
print(count)
// -> 55
```

range(1, 11) 은 숫자 1부터 10까지의 숫자를 데이터로 갖는 객체이다. 따라서 위 예에서 변수 i 에 1부터 10까지 하나씩 차례로 대입되면서 count = count + i 문장을 반복적으로 수행하고 count 는 최종적으로 55가 된다.

앞에서 살펴본 "60점 이상이면 합격" 문장을 출력하는 예제도 range 함수를 사용해서 바꿀 수 있다.

```python
count = [90, 25, 67, 45, 80]
for i in range(len(count)):
		if count[i] < 60 :
				continue
		print(f'{count}번 학생 합격입니다. 축하합니다.')
```

### for문과 range를 이용한 구구단

```python
for i in range(2, 10) :       #1번 for문
		for j in range(1, 10):    #2번 for문
				print(i * j, end=" ")
		print(' ')
// -> 
2 4 6 8 10 12 14 16 18 
3 6 9 12 15 18 21 24 27 
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54 
7 14 21 28 35 42 49 56 63 
8 16 24 32 40 48 56 64 72 
9 18 27 36 45 54 63 72 81
```

위 예제를 보면 for문을 두번 사용했다. 1번 for문에서 2부터 9까지의 숫자가 차례대로 i에 대입된다. i가 처음 2일 때 2번 for문을 만나게 된다. 2번 for문에서 1부터 9까지의 숫자가 j에 대입되고 그 다음 문장 print(i * j)를 실행한다.

따라서 i가 2일 때 2 * 1, 2 * 2 , 2* 3, ... 2 * 9 까지 차례대로 실행되며 그 값을 출력하게 된다. i가 3일 때 2일 때와 마찬가지로 실행되고 i가 9일 때까지 계속 반복된다.

## list comprehension

리스트 안에 for문을 포함하는 list comprehension을 사용하면 좀 더 편리하고 직관적인 코드를 만들 수 있다.

```python
a = [1,2,3,4]
result = []
for num in a:
		result.append(num*3)
print(result)
// -> 
[3, 6, 9, 12]
```

a 리스트의 각 항목에 3을 곱한 결과를 result 리스트에 담는 예제이다.

list comprehension을 사용하면 다음과 같이 간단하게 만들 수 있다. 

```python
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)
// ->
[3, 6, 9 ,12]
```

만약 [1, 2, 3, 4] 중에서 짝수에만 3을 곱하고 싶다면 다음과 같다.

```python
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
// ->
[6, 12]
```

list comprehension 기본 문법은 다음과 같다.

```python
[표현식 for 항목 in 반복가능객체 if 조건문]
```