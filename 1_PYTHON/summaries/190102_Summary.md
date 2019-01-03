# 190102 Summary

## 1. jupyter notebok

1) 활성화하는 법

eduyu jupyter_notebooks > clone or download > 주소 복사해서 git bash에 복붙?

* 저장: ctrl+s
* 실행: ctrl+enter
* esc를 누르면 파란색: command mode
* 커서를 두면 초록색: editor mode(or 그냥 enter)
* 단축키 보기: cmd mode에서 h
* 빠른 결과창: esc누르고 cmd mode로 변경해서 ctrl+enter(실행) 누르면 결과값이 도출됨.
* 바뀐 코드를 변경 -> 저장 -> cmd mode에서 저장하면 자동으로 밑에 값 변경.
* 아래 새로운 입력란: cmd mode에서 b(below)
* 위에 새로운 입력란: cmd mode에서 a(above)
* 셀 제거: 셀에서 dd
* []: 대괄호 안에 있는 숫자가 실행된 값
  - 따라서 reset하고 싶다면 맨 위에 있는 셀에서 cmd mode로 실행한 뒤 00을 눌러주고 kernel okay.
  - kernel > restart & clear output 누르면 도출된 결과값들 모두 제거됨.





## 2. Python

1. 파이썬에서 내장함수로 쓰이고 있는 키워드들 소환

   ```python
   import keyword
   print(keyword.kwlist)
   ```



2. 개발자가 남긴 메모만 읽기

   ```python
   def ss3(a, b):
   	"""
   	멀티스퀘어 703호
       반장: 황은석
       총무: 
       새해복 많이 받으세요
       """
       return(a + b)
   
   print(ss3.__doc__) 
   #라고 치면 개발자가 남긴 장문의 메모만 읽을 수 있다.
   ```



3. 코드를 이어서 쓸 수 있을까?

   ```python
   #이 따위로도 이어서 쓸 수 있음
   print('ss3'); print('coding')
   ```



4. 너무 긴 코드를 끊어서 쓸 수 있을까?

   ```python
   a = 'hi'
   if a == 'hi':
       print(a)
       
   a = 'hi'
   if a \ #역슬래쉬를 사용하면 가능. 아무데서나 끊을 수 있음.
   == 'hi':
       print(a)
   ```



5. id(x)

   ```python
   x = 1
   print(id(1))
   1426680576 #정수 1과 같은 경우엔 파이썬 메모리에 고정 주소값이 있음
   
   x = 1004
   print(id(1004))
   2351053432784 #but 2^8 이상의 숫자는 랜덤 주소값 출력
   ```



6. 파이썬에서만, 같은 값을 동시에 할당할 수 있다.

   ```python
   x = y = 100
   print(x)
   print(y)
   
   100
   100
   ```


7. 다른 값을 동시에 할당할 수도 있다.

   ```python
   a = 1
   b = 2
   
   # tmp = a #tmp는 변수
   # a = b
   # b = tmp
   
   print(a)
   
   
   a, b = 1, 2
   a, b = b, a
   
   print(a)
   print(b)
   ```


8. 2진수 계산

   ```python
   # n진수 2, 8, 10, 16진수를 보통 많이 사용한다.
   
   binary_num = 0b100 #b이후의 숫자를 n진수로 바꿔라.
   print(binary_num)
   
   octal_num = 0o100
   print(octal_num)
   
   decimal_num = 2019
   print(decimal_num)
   
   hexadecimal_num = 0xfff #16진수는 4자리수로 사용.
   print(hexadecimal_num)
   
   
   print('''
   2진수: {}, 
   8진수: {}, 
   10진수: {}, 
   16진수: {}
   '''.format(binary_num, octal_num, decimal_num, hexadecimal_num))
   ```



9. 부동소수점

   ```python
   b = 314e-2
   b
   
   b = 314 * 10 ** -2
   
   #위와 아래는 3.14로 모두 같다.
   ```



10. 실수 표현 오류

    ```python
    0.1 * 3
    0.30000000000000004 
    
    
    a = 0.1 * 3
    b = 0.3
    
    a - b
    5.551115123125783e-17 
    #가끔 이런 오류가 남.
    ```

    ```python
    #처리방법 1-1. 절대값을 비교
    
    a = 0.1 * 3
    b = 0.3
    
    abs(a - b) <= 1e-10
    #1의 -10진수보다 훨씬 작으면 사실상 무시하자.
    ```

    ```python
    # 처리방법 1-2. 절대값 비교를 내장된 float epsilon값과 비교
    
    import sys
    abs(a - b) <= sys.float_info.epsilon
    #시스템에서 쓸 수 있는 가장 작은(epsilon) 실수보다 작으면 무시하자.
    ```

    ```python
    # 처리방법 2. math 모듈을 통해 근사한 값인지 비교
    # python 3.5부터는 math 모듈을 활용할 수 있다.
    
    import math
    math.isclose(a, b)
    #a와 b가 정말 가까운 값이냐, 맞으면 T 틀리면 F
    ```

* ` != ` 표현은 '같지 않다'라는 뜻.
* 0/None/[], {}, (), '' 등 없거나 비어 있으면 무조건 F, 나머지 숫자는 무조건 T, 



11. 문자열 안 문장부호 사용

    ```python
    print('스티브 잡스가 말하길, \'Real Artist Ship\'')
    print('스티브 잡스가 말하길, "Real Artist Ship"')
    print("He saids, 'Real Artist Ship'")
    
    #서로 중복되지 않도록
    #문자열 안에 문장부호(', ")가 활용될 경우 이스케이프 문자(\)를 사용하는 것 대신 활용 가능 
    ```


12. 변수를 문자열에 바로 넣고 싶을 때, format 사용

    ```python
    name = 'Ben'
    print("""
    my name is {}
    """.format(name))
    
    my name is Ben
    ```


13. 이스케이프 문자열

    | 예약문자 | 내용(의미)      |
    | -------- | --------------- |
    | \n       | 줄바꿈          |
    | \t       | 탭              |
    | \r       | 캐리지리턴      |
    | \0       | 널(Null)        |
    | `\\`     | `\`             |
    | '        | 단일인용부호(') |
    | "        | 이중인용부호(") |

* `end=` 백슬래시 기능. 괄호 안에 부등호가 있는 경우엔 무조건 띄어쓰기 하지 않음. 
* print문에 한 줄 띄어쓰기를 하고 싶을 때, \n을 + '\n'의 형태로 집어넣을 수 있음.



14. string interpolation

    1) `%-formatting`: %는 place holder

    ```python
    name = 'Ben'
    print('Hello %s' % name)  # %s가 일종의 컵홀더 같은 느낌
    
    'Hello Ben'
    
    name = "철수"
    print('"안녕, %s야"' % name)
    
    "안녕, 철수야"
    ```

    2) [`str.format()`](https://pyformat.info/)

    ```python
    'Hello, {}'.format(name)
    ```

    3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.

    ```python
    name = 'Ben'
    year = 2019
    
    f'Hello, {name}, It\'s {year}'
    
    "Hello, Ben, It's 2019"
    ```

    * 짬뽕

      ```python
      f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}'
      
      '오늘은 19년 01월 02일 Wednesday'
      
      # 이때 %A는 그냥 디폴트값으로 요일을 호출함. 변경X 이유X
      ```

    * 연산도 가능

      ```python
      pi = 3.1415926535
      f'원주율은 {pi:0.3}, 반지름이 2인 원의 넓이는 {pi*2*2}'
      
      '원주율은 3.14, 반지름이 2인 원의 넓이는 12.566370614'
      
      #첫번째 포맷에서 콜론과 숫자는 소숫점 n번째에서 자르라는 의미
      ```



15. 연산자

    | 연산자 | 내용           |
    | ------ | -------------- |
    | +      | 덧셈           |
    | -      | 뺄셈           |
    | *      | 곱셈           |
    | /      | 나눗셈         |
    | //     | 몫             |
    | %      | 나머지(modulo) |
    | **     | 거듭제곱       |

* divmod(a, b): b를 a로 나눈 몫과 나머지가 출력

  ```
  #로 넣으면 각자 출력값이 들어감
  
  quotient, remainder = divmod(5, 2)
  print(f'몫은 {quotient}, 나머지는 {remainder}')
  
  몫은 2, 나머지는 1
  ```

* 양수, 음수 전환: -만 붙여주면 됨. 반대로 --를 두 번 붙이면 양수가 됨.

  ```
  positive_num = 4
  print(-positive_num)
  
  -4
  ```


16. 비교 연산자

    | 연산자 | 내용     |
    | ------ | -------- |
    | a > b  | 초과     |
    | a < b  | 미만     |
    | a >= b | 이상     |
    | a <= b | 이하     |
    | a == b | 같음     |
    | a != b | 같지않음 |

* 3.0 == 3 는 True

* 'HI' == 'hi'는 False 

  사람다운지, 아닌지? 근데 딱히 납득이 잘 안 간다. 동일원리가 적용되지 않아서 뭔가 컴퓨터답지가 않음.



17. 논리 연산자

    | 연산자  | 내용                         |
    | ------- | ---------------------------- |
    | a and b | a와 b 모두 True시만 True     |
    | a or b  | a 와 b 모두 False시만 False  |
    | not a   | True -> False, False -> True |

* print(True and False and True): False. 하나라도 거짓이라면 모두 거짓. ex) 비밀번호 입력, 찾기
* print(True or False or False): True. 하나라도 참이면 모두 참. 

* print(not True); print(not 0); print(not True and not 0); print(not 0 and not [] and not ''): F, T, F, T.

* ```python
  print(3 and 5)
  print(0 and 3)
  print(3 and 0)
  print(0 and 0)
  
  5
  0
  0
  0
  
  #왜?
  #2, 3, 4는 False이긴 하지만 0이 들어가 있으니까 0으로 그냥 출력됨. 사실상 F와 같음.
  #1의 경우엔 뒤의 숫자가 그대로 출력됨. 마지막으로 본 숫자가 출력.
  ```

* ```python
  print(3 or 5)
  print(0 or 3)
  print(3 or 0)
  print(0 or 0)
  
  3
  3
  3
  0
  
  #이것도 마찬가지. or니까 T값이 나와버리면 뒤까지 더이상 볼 필요가 없어 앞의 숫자 출력.
  ```



18. 복합 연산자

    | 연산자  | 내용       |
    | ------- | ---------- |
    | a += b  | a = a + b  |
    | a -= b  | a = a - b  |
    | a *= b  | a = a * b  |
    | a /= b  | a = a / b  |
    | a //= b | a = a // b |
    | a %= b  | a = a % b  |
    | a **= b | a = a ** b |

* 연산자와 = : 연산과 대입을 한번에 하는 것(그렇지 않으면, 대입을 따로 해야 하니까)

  ```python
  a = 1
  a = a + 1
  a += 1
  print(a)
  
  b = 10
  b *= 5
  print(b)
  ```

* 0부터 n번째까지 카운트하기

  ```python
  count = 0
  while count < 5:
      print(f'{count} 번째 얍!')
      count += 1
  ```


19. 기타 연산자

    ### Concatenation

    숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있다.

    ```python
    print('hi' + ' 2019')
    print([1] + [2, 3])
    
    hi 2019
    [1, 2, 3]
    ```

    ### Containment Test

    `in` 연산자를 통해 속해있는지 여부를 확인할 수 있다.

    ```python
    print('a' in 'apple')
    print('p' and 'e' in 'apple')
    print(1 in [1, 2, 3])  #리스트 안에서도 특정 개체를 찾을 수 있고
    print('b' in ('a', 'b', 'c'))  #튜플 안에서도 특정 개체를 찾을 수 있다.
    
    True
    True
    True
    True
    
    
    print(3 in range(10))
    print(10 in range(10))
    
    True
    False  #왜냐하면 range 함수는 9까지만 포함하고 있으니까.
    ```

    ### Identity

    `is` 연산자를 통해 동일한 object인지 확인할 수 있다.

    (나중에 Class를 배우고 다시 학습)

    ```python
    a = 10
    b = 10
    print(a == b)
    print(a is b)
    
    True
    True  #==와 is는 분명히 다른데 왜 같은 값?: is는 id 주소값 출력이라서.
    
    
    x = 257
    y = 257
    print(x == y)
    print(x is y)
    
    True
    False  #2**8까지는 저장돼 있지만 그 이상은 없어서 False로.
    ```

    ### Indexing/Slicing

    `[]`를 통한 값 접근 및 `[:]`을 통한 슬라이싱

    (다음 챕터를 배우면서 추가 학습)

    ```python
    print([1, 2, 3][0])
    print(('a', 'b', 'c')[1])
    print('apple'[4])
    print({1, 2, 3}[0])
    
    1  #리스트, 튜플에서는 순서가 중요하기 때문에 가능하고 스트링 값도 출력 가능.
    b
    e
    Error  #왜냐하면 세트는 무질서 주머니와 같기 때문에 순서가 존재하지 않기 때문이다.
    ```


20. 연산자 우선순위
    1. `()`을 통한 grouping
    2. Slicing
    3. Indexing
    4. 제곱연산자 **
    5. 단항연산자 +, - (음수/양수 부호)
    6. 산술연산자 *, /, %
    7. 산술연산자 +, -
    8. 비교연산자, `in`, `is`
    9. `not`
    10. `and`
    11. `or`



21. 기초 형변환(Type Conversion)

    1) 암시적 형변환(Implicit Type Conversion)

    - bool

    - Numbers (int, float, complex)

      ```python
      #1
      print(True + 3)
      4
      
      
      #2
      int_num = 3
      float_num = 5.0
      complex_num = 3+5j
      
      print(int_num + float_num)
      8.0
      
      
      #3
      print(int_num + complex_num)
      6+5j
      ```




​	2) 명시적 형변환(Explicit Type Conversion)

​		- 형식에 맞는 숫자만 가능

​		- str은 글씨가 숫자일 때만 형변환이 가능

​		- int -> str은 가능하지만, (숫자가 아닌 그냥) str -> int는 불가능

​		- int에 실수를 쓰면 정수값만 자동 반환

```python
#1
print(1 + '등')
에러
```

```python
#2
print(str(1) + '등')   
'1등'
```

```python
#3
print('10010')
10010  #문자열이지만 형식에 맞는 숫자이기 때문에 숫자가 출력.
```

```python
#4
print(int(3.5))
3  
  
#소숫점 이하 버림. 정수값만 출력.
```


22. 시퀀스 자료형

    - 기본적으로 시퀀스 타입은 리스트, 튜플, 레인지, 문자열, 바이너리(따로 다루진 X)
    - 순서대로 나열되었지만, 그것이 순서대로 정렬되었다는 뜻은 아님.
    - 리스트: cf) 특히, 리스트에서 특정 값만 꺼내고 싶을 때

    ```python
    locations = ['서울', '대전', '광주', '구미']
    print(locations[0])
    
    서울
    ```

    - 레인지: range(n, m)의 경우에 n부터 m-1까지 나열. range(n, m, s)의 경우에 n부터 m-1까지 s만큼 나열

    ```python
    #5의 배수로 100에서부터 숫자를 줄여 나열하라
    list(range(100, 0, -5))
    ```

    * 튜플: 리스트와 유사하지만 ()로 묶어 표현하고, 수정 불가능하며 읽기와 덮어쓰기만 가능

```python
is_tuple = 'a', 'b'
print(type(is_tuple))

is_tuple = 'c'
print(is_tuple)
c
```



23. 시퀀스에서 활용할 수 있는 연산자/함수

    | operation  | 설명                    |
    | ---------- | ----------------------- |
    | x in s     | containment test        |
    | x not in s | containment test        |
    | s1 + s2    | concatenation           |
    | s * n      | n번만큼 반복하여 더하기 |
    | s[i]       | indexing                |
    | s[i:j]     | slicing                 |
    | s[i:j:k]   | k간격으로 slicing       |
    | len(s)     | 길이                    |
    | min(s)     | 최솟값                  |
    | max(s)     | 최댓값                  |
    | s.count(x) | x의 갯수                |

* ```python
  #1
  string = 'my string'
  print('y' in string)
  
  
  #2
  l = [1, 2, 3]
  print(1 in l)
  print(2 not in l)
  
  True
  False
  
  
  #3
  print('happy' + 'hacking')
  print(['a', 'p', 'p'] + ['l', 'e'])
  
  happyhacking
  ['a', 'p', 'p', 'l', 'e']
  
  
  #4
  print('x' * 10)
  print([1, 2, 3] * 10)
  
  xxxxxxxxxx
  [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
  
  
  #5
  names = ['벤', '준', '백준', '오리']
  ca = names[0]
  print(ca)
  
  
  #6
  neo_list = names[1:3]
  print(neo_list)
  
  ['준', '백준']
  
  
  #7
  r = range(30)
  print(len(r)) #개수
  
  30
  
  r = r[0:len(r):3]
  print(r)
  
  range(0, 30, 3)
  
  
  #8
  print(list(r))
  
  [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
  
  
  #9
  print(list(r)[1:])
  
  [3, 6, 9, 12, 15, 18, 21, 24, 27]
  
  
  #10
  li = [1, 2, 3, 4, 5, 6, 7]
  li.count(5)
  
  print([1, 2, 3, 4, 5, 6, 7].count(5))
  
  1
  ```

* in 연산자는 오직 시퀀스에서만 가능



24. 세트
    * 순서가 없고, 중복값이 없다.
    * {}

| 연산자/함수       | 설명   |
| ----------------- | ------ |
| a - b             | 차집합 |
| a \| b            | 합집합 |
| a & b             | 교집합 |
| a.union(b)        | 교집합 |
| a.intersection(b) | 교집합 |

```python
my_number = {1, 2, 3, 4, 5, 6}  
lotto = {1, 2, 4, 5, 8, 9}
print(my_number & lotto)  #'&' 교집합

#근데 여기에 1, 2를 중복해서 써도 에러가 안 남. 
#고로 사용자가 알아서 중복값없이 잘 입력해야 함.
```

```python
overlap = [1, 2, 3] * 10
my_set = set(overlap)
unique = list(my_set)
print(unique)

#리스트 -> 세트 -> 리스트로 출력하면 중복값이 싹 제거가 됨. 
# 세트로 변형하면서 중복값이 삭제되니까.
```



25. 딕셔너리

    * { key:value }로 이뤄져 있음
    * 역시 {}. but 그냥 공백으로 두면 dict 타입으로 뜸
    * 앞 뒤는 공백인 게 convention

    ```python
    ss3 = { 'leader':'황은석', 'ca':'강' }
    print(ss3['leader'])
    
    황은석
    
    #딕셔너리에서 value값은 그에 맞는 키값을 따옴표 사이에 넣어 입력해주면 됨
    ```

    ```python
    my_dict = { 1:1, 1:2, 2:1, 3:2 }
    print(my_dict)
    
    {1: 2, 2: 1, 3: 2}
    
    #중복된 key는 존재할 수 없음
    #출력해도 중복key는 자동 삭제됨
    ```

    ```python
    print(ss3.keys())
    print(ss3.values())
    
    dict_keys(['leader', 'ca'])
    dict_values(['황은석', '강'])
    
    #키값과 밸류값만 따로 묶어서 꺼낼 수 있음
    ```

    ![](C:\Users\student\Downloads\container.png)