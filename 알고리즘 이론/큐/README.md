# 큐(Queue)

### 큐란?

- 큐는 선입선출(First In First Out; FIFO)의 특성을 가지는 추상 자료형이다.
- 입력된 데이터가 순서대로 처리되어야 할 때 사용한다. (First Come, First Served.)

## 큐의 구현

## 선형 큐(Linear Queue)

<img width="1034" alt="스크린샷 2021-06-25 오후 7 50 05" src="https://user-images.githubusercontent.com/77820288/123423678-d199f400-d5fa-11eb-8be5-bf1ef8935edc.png">


```python
# 선형큐
class Queue :
    
    def __init__(self, Qsize) :
        self.front = 0
        self.rear = 0
        self.capacity = Qsize
        self.List = [None] * self.capacity
        
    def isEmpty(self) :
        flag = False
        if self.front == self.rear :
            flag = True
        return flag
    
    def append(self, value) :
        self.List[self.rear] = value
        self.rear += 1
    
    def popleft(self) :
        if not self.isEmpty() :
            answer = self.List[self.front]
            self.List[self.front] = None
            self.front += 1
            return answer
        else :
            return None
    def show(self) :
        out = []
        out = self.List[self.front:self.rear]
        return out
    
Q = Queue(5)
Q.append(3)
Q.append(5)
Q.append(7)
Q.show()
print(Q.popleft())
Q.show()
```

매직메서드인 init 함수를 사용해 클래스 Queue 는 Q의 사이즈를 인자로 받는다.

그리고 맨 처음을 가리키는 front와 맨 마지막을 가리키는 rear를 0으로 초기화 시켜준다.

인자로 받은 Q 사이즈를 self.capacity에 할당한다.

Q 사이즈만큼의 길이를 가진 None 값으로 채워져 있는 리스트를 self.List에 할당해준다.

isEmpty → 맨 처음을 가리키는 front와 맨 마지막을 가리키는 rear가 같은 곳을 가리킬 때 큐가 비어있다는 것을 알 수 있다. 

append → 리스트에 추가할 값을 value라는 변수에 할당한다. 그리고 인자로 받은 값을 리스트의 맨 마지막에 할당 후 self.rear는 다음 인덱스를 가리킨다.

popleft → 기본적으로 파이썬의 pop은 리스트의 맨 처음 값을 꺼낸다. 

만약 큐가 비어있지 않다면 리스트의 맨 처음 값을 할당 한 변수 answer를 None으로 바꾼 후 self.front는 그 다음 인덱스를 가리킨다.

show → 빈 리스트를 변수 out에 할당한다. 그리고 슬라이싱을 이용하여 front부터 rear까지의 값을 out에 할당한다.

## 원형 큐(Circular Queue)

<img width="1028" alt="스크린샷 2021-06-25 오후 7 50 36" src="https://user-images.githubusercontent.com/77820288/123423716-dd85b600-d5fa-11eb-8826-76f86416169b.png">

 

```python
# 원형큐
class Queue :
    
    def __init__(self, Qsize) :
        self.front = 0
        self.rear = 0
        self.capacity = Qsize
        self.List = [None] * self.capacity
        
    def isEmpty(self) :
        flag = False
        if self.front == self.rear and self.List[self.front] == None :
            flag = True
        return flag
    
    def isFull(self) :
        flag = False
        if self.front == self.rear and self.List[self.front] != None :
            flag = True
        return flag
    
    def append(self, value) :
        if not self.isFull() :
            self.List[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity
            return True
        else :
            return False
    
    def popleft(self) :
        if not self.isEmpty() :
            answer = self.List[self.front]
            self.List[self.front] = None
            self.front = (self.front + 1) % self.capacity
            return answer
        else :
            return None
    def show(self) :
        out = []
        if self.isFull() :
            out = self.List[self.front: ] + self.List[ :self.rear]
        elif not self.isEmpty() :
            if self.front < self.rear :
                out = self.List[self.front:self.rear]
            else :
                out = self.List[self.front: ] + self.List[ :self.rear]
        return out
    
Q = Queue(5)
Q.append(3)
Q.append(5)
Q.append(7)
Q.append(9)
Q.append(11)
print(Q.show())
print(Q.popleft())
print(Q.show())
```

선형 큐와 비슷하지만 다른 부분이 있다.

isEmpty → 만약 맨 앞부분과 맨 끝부분이 같거나 리스트의 맨 앞부분이 None이라면 비어있다고 본다.

isFull → 위와 반대로 맨 앞부분과 맨 끝부분이 같거나 리스트의 맨 앞부분이 None이 아니라면 리스트가 꽉차있다고 본다.

append → 만약 리스트가 꽉 차있는게 아니라면 리스트에 추가할 값을 value라는 변수에 할당한다. 그리고 리스트 길이를 맨 끝부분 + 1 값으로 나눈 나머지 값을 self.rear에 할당한다. 즉 마지막 부분에 들어온 값을 할당 후 rear는 그 다음 인덱스를 가리키게 된다.

ex) 5를 1로 나눈 나머지 값은 1, 2로 나눈 나머지 값은 2이다. 

popleft → 만약 리스트가 비어있는게 아니라면 리스트에 추가할 값을 answer라는 변수에 할당한다. 

그리고 리스트 맨 앞부분을 None으로 바꾸고 리스트 길이를 맨 앞부분 + 1 값으로 나눈 나머지 값을 self.front에 할당한다. 즉 맨 앞부분을 None으로 바꾸고  slef.front는 그 다음 인덱스를 가리키게 된다.

show → 여기서 show는 여러가지 경우로 나뉜다.

1. 리스트가 꽉 차 있는 경우
2. 리스트가 비어있지 않는 경우
    1. 비어있지 않는 경우에서 맨 앞부분의 값이 끝부분의 값보다 작은 경우
    2. 비어있지 않는 경우에서 맨 앞부분의 값이 끝부분의 값보다 큰 경우

## 연결리스트 큐(Linked Queue)



```python
# 링크 큐
class Node :
    def __init__(self, value, prev, next) :
        self.value = value
        self.prev = prev
        self.next = next

class LinkedQueue:
    def __init__(self):
        self.Head = None
        self.Tail = None
        
    def append(self, value) :
        if self.Head is None :
            self.Head = Node(value, None, None)
            self.Tail = self.Head
        else :
            self.Tail.next = Node(value, self.Tail, None)
            self.Tail = self.Tail.next
            
    def popleft(self):
        if self.Head is None :
            return None 
        if self.Head == self.Tail :
            answer = self.Head.value
            self.Head = None
            self.Tail = None
            return answer
        
        answer = self.Head.value
        self.Head = self.Head.next
        self.Head.prev = None
        return answer
    
    def show(self) :
        s = '['
        
        curr = self.Head
        while curr is not None:
            s = str(curr.value) + ','
            curr = curr.next
            
        s += ']'
        print(s)

Q = LinkedQueue()
Q.append(1)
```

링크리스트 큐는 다른 말로 노드로 구현된 큐라고 볼 수 있다.

각각의 노드는 Head와 Tail을 가지고 있다.

append → 만약 Head가 None이라면 Head와 Tail은 인자로 들어온 value값을 갖는다.

만약 Head가 None이 아니라면 새로 생긴 노드에 인자로 받은 값을 할당하고 Head와 같은 값을 바라보고 있던 Tail은 새로 생긴 노드의 값을 바라본다.

popleft → 만약 Head가 None이라면 None을 리턴하고 만약 Head와 Tail의 값이 같다면(노드가 1개밖에 없는 경우) 원래 있던 값을 answer에 할당 후 Head와 Tail을 None으로 바꿔준다.

위의 경우에 해당하지 않다면 원래 있던 값을 answer에 할당한다. 그리고 Head는 다음 노드를 가리키고 원래 있던 Head를 None으로 바꿔준다.

### 재귀함수(Recursive)

```python
def DFS(n):
    if n == 0:
        return 
    else :
        print(n, end='')
        DFS(n-1)
        
DFS(3)
```

재귀함수란 함수 내부에서 자기함수를 호출하는 함수이다. 재귀함수는 스택프레임을 사용하고 있다. 즉, 

후입선출(Last In First Out; LIFO)의 형태이다.

```python
# 피보나치(재귀)
def fibo(n):
    if n <= 2 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
    
fibo(35)
```

피보나치 수열을 재귀함수로 구현 후 호출하면 호출되기까지 약 2~3초가량 소요된다.

따라서 재귀함수는 함수 내부에서 자신을 또 호출하기 때문에 인자값이 커지면 소요시간이 기하급수적으로 증가한다. 이러한 단점을 해결하기 위해선 메모리제이션(memoization)을 사용하는 방법이 있다.

- 메모이제이션(memoization)은 컴퓨터 프로그램이 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술이다.

```python
# 메모리제이션
def fibo(n):
    if dy[n] > 0 :
        return dy[n]
    if n <= 2 :
        return 1
    else :
        dy[n] = fibo(n-1) + fibo(n-2)
        return dy[n]
dy = [0] * 50
fibo(40)
```

재귀함수로 얻어지는 값들을 해당하는 인덱스의 값으로 저장 후 같은 함수를 또 다시 호출하게 되는 일이 발생했을 때 탐색을 하지 않게끔 구현한다. 이런식으로 구현된 재귀함수의 호출되는 소요시간은 인자값이 위의 값보다 큼에도 불구하고 약 0.1초가량 소요된다.