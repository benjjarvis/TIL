# 090103 Summary

## 1. Python Control of Flow

### 1) Basic Rules of Conditions

1. if문은 반드시 일정한 참/거짓을 판단할 수 있는 조건식과 함께 사용돼야 한다.
2. 조건이 참인 경우: ':' 이후의 문장을 수행한다.
3. 조건이 거짓인 경우: 'else:' 이후의 문장을 수행한다.

* 반드시 **들여쓰기(indenting)** 할 것. 파이썬에서는 들여쓰기로 판단.
* PEP-8에서 권장하는 4 time spaces를 사용할 것.



### 2) Basic Usage of Conditions

* **input()**: 사용자가 입력한 값을 받는 함수. 빈칸이 나옴. 기본적으로 <u>string으로 저장</u>.
* ex) user_input = input()을 쓰게 되면, 입력한 값을 user_input이라는 박스에 넣음.

```python
number = input()
number = int(number)

# 위의 과정을 한 줄로 축약하면,
number = int(input(number))

# "점수를 입력하세요 : 3"를 입력 후 홀/짝 판단을 하게 하려면?
number = int(input("점수를 입력하세요 : "))

if number % 2 == 1:
    print('홀수입니다')
else:
    print('짝수입니다')
```



### 3) Conditions - Plural

* 2개 이상의 조건문을 활용할 경우, **elif 조건식**을 활용한다.

```python
# 조건문을 통해 변수 score에 입력한 평점을 출력하고 싶다면?
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```



### 4) Conditions - Reiteration

```python
# 위의 실습 코드를 활용하여 95점 이상이면, "참잘했어요"를 함께 출력
score = int(input("점수를 입력하세요 : "))

if score >= 90
    print('A')
    if score >= 95:
        print('참 잘했어요')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
    
    
# 3의 배수는 Fizz, 5의 배수는 Buzz, 3과 5의 배수는 FizzBuzz가 나온다.
n = int(input("숫자를 입력하세요: "))

for i in range(1, n+1):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
```



### 5) Conditional Expression

* if, else를 보통 많이 사용하는데 일일히 쓰는 게 귀찮으니 축약식으로 표현하는 방법

  ```python
  num = 3
  print('3이네') if num == 3 else print('3이 아니네')
  # 영문법식으로 생각하면 됨. Do '3이네' if number = 3 or '3이 아니네'
  
  
  num = int(input("숫자를 입력하세요 : "))
  value = num if num >= 0 else 0 
  print(value)
  # num이 0과 같거나 크면 num, 그게 아니면 0의 결과값을 value에 집어넣어라
  
  
  if num >= 0:
      num = num
  else:
      num = 0
  print(num)
  # 위에 코드 풀어쓴 것
  
  
  num = 2
  if num % 2:
      result = '홀수입니다.'
  else:
      result = '짝수입니다.'
  print(result)
  # num % 2 == 1에서 == 1이 없어도 되는 이유는, 나머지가 0(짝수)일 경우에 0은 False이기 때문에 자동으로 else 구문으로 들어가고, 1(홀수)일 경우에 1은 True이기 때문에 자동으로 if 구문으로 들어가기 때문에 굳이 쓸 필요는 없음.
  
  
  num = 2
  result = '홀수입니다' if num % 2 else '짝수입니다'
  # 위에 코드와 같은 것
  ```



### 6) Reiteration - While

​	1) 조건식이 **참인 경우 반복적인 코드**를 실행하는 문법

​	2) **종료조건을 반드시 설정**해주어야 한다(그렇지 않을 경우 계속해서 반복)

​	![](C:\Users\student\Downloads\while.png)

```python
a = 0

while a < 5:
    print(a)
    a += 1

print("끝")
```

* but, while문은 잘못 쓰면 느려지거나 멈추기 때문에 거의 쓰지 않는다고 함



### 7) Reiteration - for

​	1) 정해진 범위 내(시퀀스)에서 순차적으로 코드를 실행하는 문법

​	- **for문 안에서의 print**는 밖에 쓰지 않고 **안에 써야함**. 반드시 지킬 것. 

```python
for x in range(10):
    print(x)
# 정상적인 문법에선 for문 안에서 print(x)를 출력해야 함

print(x)
# 밖에서 print(x)를 찍어보면 마지막 변수인 9만 출력
```

```python
# 반복문과 조건문만 활용하여 1~30까지 숫자 중에 홀수만 담긴 리스트 만들기
# 1
odd_num = []
for x in range(1, 31):
    if x % 2 == 1:
        odd_num.append(x)

print(odd_num)


# 2; .append()를 쓰지 않고 출력하는 방법
odd_num = []
for x in range(1, 31):
	if x % 2 == 1:
        odd_num = odd_num + [x]

print(odd_num)



# 1부터 100까지 자연수 중 5의 배수들의 총합을 구하라
# 1
five_sum = []
for x in range(1, 101):
    if x % 5 == 0:
        five_sum = five_sum + [x]

print(sum(five_sum))


# 2
s = 0
for i in range(1, 21):
    s += i
result = s * 5

print(result)


# 3
s = 0
for i in range(1, 21):
    s += i * 5

print(s)
```



#### 7-1) Using for reiteration with index function

* enumerate() 함수를 활용하면, 추가적인 변수를 활용할 수 있다. 순서 지켜주는 게 좋음.

* enumerate()는 파이썬 내장함수이며, 다음과 같이 구성돼 있다.

  : 기본적으로 튜플 형태로 출력함

  : 또한, 기본적으로 인덱싱의 start 값은 0

* ```python
  todays_menu = ['생선까스', '북어해장국', '비엔나소세지']
  
  for index, menu in enumerate(todays_menu):
      print(index, menu)
  ```

* ```python
  mates = ['박준태', '박찬미', '백지원', '송건호', '안도건']
  list(enumerate(mates))
  
  [(0, '박준태'), (1, '박찬미'), (2, '백지원'), (3, '송건호'), (4, '안도건')]
  
  
  list(enumerate(mates, start = 1))
  
  [(1, '박준태'), (2, '박찬미'), (3, '백지원'), (4, '송건호'), (5, '안도건')]
  ```



#### 7-2) Using for reiteration with dictionary

* 딕셔너리 형태에서 키값, 밸류값을 출력하고 싶다면

* ```python
  classroom = { 'teacher': 'Yu', 'leader': 'Hwang', 'CA': 'Kang' }
  
  # 1
  print(classroom['teacher'])
  
  # 2
  for member in classroom:
      print(member, classroom[member])
  
  # 3
  for role in classroom:
      print(classroom[role])
      
      
  Yu
  
  teacher Yu
  leader Hwang
  CA Kang
  
  Yu
  Hwang
  Kang
  ```

* 딕셔너리에서 for를 활용하는 4가지 방법:

* ```python
  # 0. dictionary (key 반복)
  for key in dict:
      print(key)
  
  # 1. key 반복
  for key in dict.keys():
      print(key)
  
  # 2. value 반복    
  for val in dict.values():
      print(val)
  
  # 3. key와 value 반복
  for key, val in dict.items():
      print(key, val)
  ```



#### 7-3) Break in reiteration for

* break는 반복문을 종료할 때 쓰는 구문으로써 for문 안에 사용한다.

* ```python
  for i in range(10):
      if i == 6:
          break
      print(i)
      
  0
  1
  2
  3
  4
  5
  ```



#### 7-4) Continue in reiteration for

* continue는 continue 이후의 코드를 수행하지 않고 자동으로 반복 수행하도록 한다.

* ```python
  for i in range(6):
      if i % 2 == 0:
          continue
      print(f'{i} is odd number')
      
  1 is odd number
  3 is odd number
  5 is odd number
  
  # 만약 continue가 없으면, 0부터 5까지 모두 출력됨
  ```



#### 7-5) Else in reiteration for

* else는 끝까지 반복문을 시행한 이후에 실행된다.

* break를 통해 중간에 종료되지 않은 경우에만 실행.

* ```python
  for i in range(3):
      if i == 3:
          print(f'{i}에서 break 실행됨')  # 여기서 걸리지 않으니까
          break
  else:								  # 여기서 걸림
      print('break 안 걸림')
    
  
  break 안 걸림
  ```

* ```python
  for i in range(3):
      if i == 2:
          print(f'{i}에서 break 실행됨')   # 여기서 실행됨
          break
  else:
      print('break 안 걸림')
      
      
  2에서 break 실행됨
  ```



### 8) Purpose of Function

* 특정 기능을 하는 코드 덩어리(편의상 함수를 사용)

* **KEEP IT SIMPLE, STUPID. DON'T REPEAT YOURSELF. KEEP IT SHORT & SIMPLE.**

```python
# 직사각형의 둘레와 면적을 구하는 함수 만들기
def rectangle(width, height):
    area = width * height
    parimeter = (width + height) * 2
    print(f'직사각형 둘레: {a}, 면적: {b} 입니다.')
    
rectangle(10, 40)
```



### 9) Basic Usage of Function

1. 함수 선언은 def로 시작하여 :로 끝나고, 4 spaces indenting 필요
2. def x(a, b): 에서 a와 b는 parameter(매개변수)
3. 함수는 동작 후에 **return**을 통해 결과값을 전달할 수도 있음
4. return 값이 없으면, None을 반환

5. 기본적으로 내장돼 있는 함수들

   ```python
   dir(__builtins__)
   
   ['ArithmeticError',
    'AssertionError',
    'AttributeError',
    'BaseException',
    'BlockingIOError',
    'BrokenPipeError',
    'BufferError',
    'BytesWarning',
    'ChildProcessError',
    ...]
   ```

   * print문도 파이썬에 지정되어 내장된 함수



### 10) Return

1. def 함수에서 자주 쓰이는 return과 print의 개념 차이

   ```python
   def yes_in_yes_out(x):
       return x
   
   def yes_in_no_out(x):
       print(x)
       
   def no_in_yes_out():
       return 'ss3'
   
   def no_in_no_out():
       print('ss3')
       
   
   # 함수에 매개변수 입력값이 있다면 in이 있는 거고, 
   # return이 없다면 out이 없는 것.
   ```

   ```python
   # my_max 함수 만들기
   def my_max(num1, num2):
       if num1 > num2:
           return num1
       else:
           return num2
   
   # 한 줄로?
   def my_max_short(num1, num2):
       return num1 if num1 > num2 else num2
   
   # but max함수를 만드는 과정이므로 이걸 쓰지 않는 게 좋음.
   def my_max(a, b):
       return(max(a, b))  
   
   print(my_max(12304820498 * 2, 2 ** 1354687))
   ```

   - **<u>def 함수에서는 print를 쓰지 않아야 함</u>**. 디버깅 예외.



### 11) Default Args. Values

* 인자 = Arguments

* 함수가 호출될 때, 인자를 지정하지 않아도 기본값을 설정할 수 있다.

* ```python
  def greeting(name='ssafy'):
      return f'{name}, 안녕?'
      
  print(greeting('neo'))  
  print(greeting())
  
  # 새로 정의한 함수는 우선순위라 이 괄호 안에 있는 인자가 대입되어 가장 먼저 출력됨.
  # 그러나 일반적인 함수는 맨 처음 함수를 정의할 때 인자 안에 쓴 값이 들어감.
  ```

* ```python
  def greeting(age, name='ssafy'):
      return f'{name}은 {age}살 입니다.'
      
  greeting(1)
  greeting(0, '미래의 ssafy')
  
  'ssafy은 1살 입니다.'
  '미래의 ssafy은 0살 입니다.'
  
  
  # 단, def greeting(name='ssafy', age)라고 쓰면 에러 남.
  # 왜냐하면, 기본 매개변수 이후에 기본 값이 없는 매개변수를 사용할 수는 없기 때문에.
  # 즉, 함수 정의 매개변수 인자에는 specified arguments가 먼저 올 수 없다는 것.
  ```



### 12) Keyword Args.

* 키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있음

* ```python
  def greeting(age, name='ssafy'):
      return f'{name}은 {age}살 입니다.'
  
  greeting(30, '서른즈음에')
  greeting(name='아홉수아닌데', age=29)
  
  
  '아홉수아닌데은 29살 입니다.'
  ```

* 하지만 이렇게는 사용할 수 없음

* ```python
  greeting(name='환갑', 60)
  
  # 왜냐하면 키워드 인자는 다 쓰거나, 쓰지 않거나.
  ```

* print 함수의 default arguments

* ```python
  print('hi', end='_')
  print('hi', end='!')
  print('hi', end='^^', sep=%%%)
  
  hi_hi!
  hi
  
  # 이것보다 더 많지만, sep=' ', end=까지만.
  # print는 return 값이 설정되지 않은 함수.
  ```



### 13) 가변 인자 리스트

1. print()처럼 정해지지 않은 임의의 숫자 인자를 받기 위해서는 가변인자를 활용

2. 가변인자는 튜플 형태로 처리가 되며, *(wildcard)로 표현됨

3. 표현법: `def func(*args):` 

   ```python
   # unknown_args(1, 2, 3, 4, ['a', 'b']) 등 임의의 숫자들이라면,
   def unknown_args(*args):
       print(args, type(args))
       
   unknown_args(1, 2, 3, 4, ['a', 'b'])
   ```

* 가변 인자 리스트를 활용해 my_max 함수 재정의

  ```python
  # 1
  def my_max(*nums):
      biggest = nums[0]
      for num in nums:
           if num > biggest:
              biggest = num
      return biggest    
  
  max = my_max(1, 2, 3, 4, 5)
  print(max)
  
  
  # 2
  def second_max(*nums):
      nums = list(nums)
      sorted(nums)
      return nums[-1]
  
  max = second_max(-39, 39, 59)
  print(max)
  ```



### 14) 정의되지 않은 인자 처리

1. **kwargs를 통해 인자를 받아 처리할 수 있음
2. **kw의 의미 자체가 임시 인자를 2개 이상 사용하겠다는 의미
3. kwargs는 dict 형태로 처리가 됨

```python
# 1
def unknown_things(*args):
    return args

print(unknown_things(1, 2, 3, 4, 5))

(1, 2, 3, 4, 5)


# 2
def unknown_things(**args):
    return args

print(unknown_things(a=1, b=2, c=3))

{'a': 1, 'b': 2, 'c': 3}


# 3: 2번과 같음. 결국 2는 딕셔너리 형태로 변형해주는 것.
result = dict(한국어='안녕', 영어='hi')
print(result)

{'한국어': '안녕', '영어': 'hi'}
```



### 15) Unpacking Args. List

* **kwargs를 통해 함수에 인자를 넘기는 방법

* ```python
  def signup(username, password, password_confirm):
      if password == password_confirm:
          return True
      else:
          return False
      
  new_account = {
      'username': 'benjjarvis',
      'password': 'aldkjaldj',
      'password_confirm': 'aldkjaldj'
  }
  # signup(new_account) 백퍼 에러남
  
  signup(**new_account)
  signup(username='benjjarvis', password='aldkjaldj', password_confirm='aldkjaldj')
  # 맨 위의 코드가 아래 모양으로 펼쳐지는 것
  ```



### 16) Name Space and Scope

1. `L`ocal scope: 정의된 함수
2. `E`nclosed scope: 상위 함수
3. `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
4. `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

```python
# print(a)에 무엇이 출력되는지 확인해보세요.
a = 1

def localscope(a):
    return a

localscope(5)


# 왜 5가 출력될까?
# 함수를 정의하는 블록과 밖의 블록은 영역이 완전히 다르기 때문
# 그러므로 Local scope X -> Enclosed scope O 이므로 2순위에서 걸림
# 하지만 최대한 Local scope에서 걸리도록 하는 게 좋음. 밖에 뭐가 있을지 없을지도 모르니까.
```

```python
# 전역 변수를 바꿀 수 있나요?
global_num = 3
def localscope2():
    global_num = 5
    print(f'global_num이 {global_num}로 설정됨.')
    
localscope2()
print(global_num)

# 결론: 바꿀 수 없다. 함수 안에서 선언한 변수는 밖의 변수와 노상관.
```

```python
# 굳이 전역에 있는 변수를 바꾸고 싶다면, 아래와 같이 선언할 수 있습니다.
global_num = 3

def localscope2():
    global global_num  # 이렇게 선언해야함. 
    global_num = 5
    print(f'global_num이 {global_num}로 설정됨.')
    
localscope2()  # 반드시 실행해야함. 근데 왜 이렇게 실행해야 하는진 모르겠음.
print(global_num)
```

