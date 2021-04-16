# 클래스

클래스를 비유로 쉽게 설명하자면 

- 과자 틀 → 클래스 (class)
- 과자 틀에 의해서 만들어진 과자 → 객체 (object)

클래스로 만든 객체는 객체마다 고유한 성격을 가지고 있다. 과자 틀로 만든 A과자를 조금 베어먹더라도 다른 B, C D과자에는 아무 영향이 없는 것과 마찬가지로 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.

### 클래스의 가장 간단한 예

```python
class Cookie :
	pass

# Cookie 클래스의 객체를 만드는 방법
a = Cookie()
b = Cookie()
```

위의 클래스는 아무 기능도 갖고 있지 않은 껍질뿐인 클래스이다. 하지만 이렇게 껍질뿐인 클래스도 객체를 생성하는 기능이 있다. 과자 틀로 과자를 만드는 것처럼 이다.

객체는 클래스로 만들며 1개의 클래스는 무수히 맣은 객체를 만들어 낼 수 있다.

### 객체와 인스턴스의 차이

클래스로 만든 객체를 인스턴스라고도 한다. a = Cookie() 로 만든 a는 객체이다. 그리고 a 객체는 Cookie의 인스턴스이다. 즉, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다. "a는 인스턴스" 보다는 "a는 객체"라는 표현이 어울리며 "a는 Cookie의 객체" 보다는 "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.

## 클래스 구조

 클래스의 기본 구조

```python
class Calculator :
		def setdata(self, first, second) : # 메서드의 매개변수
				self.first = first            # 메서드의 수행문
				self.second = second          # 메서드의 수행문

a = Calculator()
a.setdata(4, 2)   # 객체를 통한 클래스의 메서드 호출
```

클래스 안에 구현된 함수는 다른 말로는 **메서드**(Method)라고 부른다.

파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용한 것이다. self 말고 다른 이름을 사용해도 상관없다.

### 메서드의 또 다른 호출 방법

잘 사용하지는 않지만 클래스를 통해 메서드를 호출하는 것도 가능하다.

```python
a = Calculator()
Calculator.setdata(a, 4, 2)
```

위와 같이 클래스이름 . 메서드 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해 주어야 한다. 

반면에 객체 . 메서드 형태로 호출할 때는 self를 반드시 생략해서 호출해야 한다.

```python
class Calculator :
		def setdata(self, first, second) :
				self.first = first         
				self.second = second   

a = Calculator()
a.setdata(4, 2) 
print(a.first)
// -> 4
print(a.second)
// -> 2
```

a 객체에 객체변수 first 와 second가 생성되었음을 확일할 수 있다.

```python
a = Calculator()
b = Calculator()

a.setdata(4, 2)
print(a.first)
// -> 4

b.setdata(3, 7)
print(b.first)
// -> 3

print(a.first)
// -> 4
```

a 객체의 first 값은 b 객체의 first 값에 영향받지 않고 원래의 값을 유지하고 있음을 확인할 수 있다. 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다. 

 

```python
a = Calculator()
b = Calculator()
a.setdata(4, 2)
b.setdata(3, 7)

id(a.first)   # a의 first 주소값을 확인
// -> 1839194944
id(b.first)   # b의 first 주소값을 확인
// -> 1839194928
```

a 객체의 first 주소 값과 b 객체의 first 주소 값이 서로 다르므로 각각 다른 곳에 그 값이 저장된다는 것을 알 수 있다. 객체변수는 그 객체의 고유 값을 저장할 수 있는 공간이다. 

### 사칙연산 기능 만들기

```python
class Calculator :
		def setdata(self, first, second) :
				self.first = first
				self.second = second
		def add(self) :
				result = self.first + self.second
				return result
		def mul(self) :
				result = self.first * self.second
				return result
		def sub(self) :
				resutl = self.first - self.second
				return result
		def div(self) : 
				result self.first / self.second
				return result 
```

```python
a = Calculator()
b = Calculator()
a.setdata(4, 2)
b.setdata(3, 8)
a.add()
// -> 6
a.mul()
// -> 8
b.add()
// -> 11
b.div()
// -> 0.375
```

## 생성자 (Constructor)

```python
a = FourCal()
a.add()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in add
AttributeError: 'FourCal' object has no attribute 'first'
```

Calculator 클래스의 인스턴스 a에 setdata 메서드를 실행하지 않고 add 메서드를 수행하면 "AttributeError: 'FourCal' object has no attribute 'first'" 오류가 발생한다. setdata 메서드를 수행해야 객체 a의 객체변수 first 와 second 가 생성되기 때문이다. 

이렇게 객체에 초기값을 설정해야 할 필요가 있을 떄는 setdata 와 같은 메서드를 호출하여 초기값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다. 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.

파이썬 메서드 이름으로 "__init__"를 사용하면 이 메서드는 생성자가 된다. 

```python
Class Calculator :
		def __init__(self, first, second) :
				self.first = first
				self.second = second
```

"__init__" 메서드는 setdata 메서드와 이름만 다르고 모든게 동일하다. 단 메서드 이름을 "__init__"으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.

```python
a = Calculator()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'
```

a  = Calculator() 을 실행할 때 생성자 "__init__" 이 호출되어 위와 같은 오류가 발생했다. 오류가 발생한 이유는 생성자의 매개변수 first 와 second 에 해당하는 값이 전달되지 않았기 때문이다.

위 오류를 해결하려면 first와 second에 해당하는 값을 전달하여 객체를 생성해야 한다.

```python
a = Calculator(4, 2)
```

위와 같이 실행하면 "__init__" 메서드의 매개변수 first에는 4, second에는 2가 대입된다.

## 클래스의 상속(inheritance)

어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만들수 있다.

기반이 되는 클래스를 부모 클래스(parent class) 또는 기반 클래스(base class), 슈퍼 클래스(super class) 라고 부르며, 물려받은 클래스를 자식 클래스(child class) 또는 파생 클래스(derived class), 서브 클래스(sub class) 라고 한다.

앞에서 Calculator 클래스는 이미 만들어 놓았으므로 Calculator 클래스를 상속하는 MoreCalculator 클래스를 간단하게 만들 수 있다.

```python
class MoreCalculator(Calculator) :
		pass
```

클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.

- class 클래스 이름(상속할 클래스 이름)
- 

MoreCalculator 클래스는 Calculator 클래스를 상속했으므로 Calculator 클래스의 모든 기능을 사용할 수 있다.

```python
a = MoreCalculator(5, 1)
a.add()
// -> 6
a.mul()
// -> 5
a.sub()
// -> 4
a.div()
// -> 5
```

### 상속을 하는 이유

보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.

"클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?"라는 의문이 들 수 있다. 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 해야 한다.

a의 b제곱($a^b$)을 계산하는 MoreCalculator 클래스를 만들어 보자.

```python
class MoreCalculator(Calculator) :
		def pow(self) :
				result = self.first ** self.second
				return result

a = MoreCalculator(5, 2)
a.pow()
// -> 25
```

상속은 MoreCalculator 클래스처럼 기존 클래스(Calculator)는 그대로 놔둔 채 클래스의 기능을 확장시킬 때 주로 사용한다.

## 메서드 오버라이딩

부모 클래스에서 정의한 메서드를 자식 클래스에서 재정의 하는것을 말한다.

```python
class ThirdCalculator(MoreCalculator) :
		def pow(self) :
				result = self.first * self.second
				return result
```

ThirdCalculator 클래스는 MoreCalculator 클래스에 있는 pow 메서드를 동일한 이름으로 다식 작성하였다. 이렇게 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다. 이렇게 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.

```python
a = ThirdCalculator(5, 2)
a.pow()
// -> 10
```

## 클래스 변수

객체변수는 다른 객체들에 영행받지 않고 독립적으로 그 값을 유지한다면

클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다.

```python
class Family :
		lastname = 'Kim'
print(Family.lastname)
// -> Kim
```

클래스 변수는 클래스이름 . 클래스 변수 로 사용할 수 있다.

또는 다음과 같이 객체를 통해서도 클래스 변수를 사용할 수 있다.

```python
a = Family()
b = Famuly()
print(a.lastname)
// -> Kim
print(b.lastname)
// -> Kim
```

만약 Family 클래스의 lastname을 'Park'으로 바꾼다면

```python
Family.lastname = 'Park'

print(a.lastname)
// -> Park
print(b.lastname)
// -> Park
```

클래스 변수 값을 변경했더니 클래스로 만든 모든 객체의 lastname 값도 모두 변경되었다. 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다.

```python
id(Family.lastname)
// -> 4480159136
id(a.lastname)
// -> 4480159136
id(b.lastname)
// -> 4480159136
```

id 값이 모두 같으므로 Family.lastname, a.lastname, b.lastname 은 모두 같은 메모리를 가리키고 있다.

클래스 변수보다는 객체변수를 사용하는 비율이 훨씬 높다.