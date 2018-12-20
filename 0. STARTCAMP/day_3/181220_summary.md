# 181220 Sum

## 1. Quiz

​	1) Lotto

```python
#내 답
my_numbers=[1, 2, 3, 4, 5, 6]
real_numbers=[1, 2, 3, 4, 5, 6]
bonus=7

for match in my_numbers:
         if match in real_numbers:
                 print(lucky_numbers.append())

*** for문을 두번 쓸 수 있었다는 걸 몰랐고, 하나씩 뽑아서 서로 비교시킬 생각을 못 했음. 너무 체계적으로 생각해보지 못한 듯함. 또한, count를 저렇게 사용할 수 있는지 몰랐음. ***



#선생님 답
my_numbers=[1, 2, 3, 4, 5, 6]
real_numbers=[1, 2, 3, 4, 5, 6]
bonus=7

count=0
for my_number in my_numbers:
	for real_number in real_numbers: 
        #이중 for문. my에서 하나 뽑고, real에서 하나 뽑아 같냐고.
        # 밑에 있는 for문이 끝나야 그 다음 for문으로 넘어갈 수 있음.
		if my_number==real_number: 
         #두 숫자가 같으면,
            count+=1 
            #1부터 세라
print(count)

if count==6:
    print(1)
elif count==5 and bonus in my_numbers:
    print(2)
elif count==5:
    print(3)
....



#선생님 답II
my_numbers=set([1, 2, 3, 4, 5, 6])
real_numbers=set([1, 2, 3, 4, 5, 6])
bonus=7

match_count=len(my_numbers & real_numbers)
print(match_count)

if match_count==6:
    print(1)
elif match_count==5 and bonus in my_numbers:
    print(2)
elif match_count==5:
    print(3)
....
```





## 2. Set

```python
리스트 = [1, 2, 3]
딕셔너리 = {1:2, 3:4}
세트 = {1, 2, 3}
```

- **집합**의 일종이기 때문에, 전혀 **순서가 없음**. 
- 따라서 세트[0] 식으로 안에 있는 것을 꺼낼 수가 없음.
- 대신에 `1 in 세트` 식으로 항목이 있는지 여부는 물어볼 수 있음.
- 리스트 -> 세트화: set()를 앞뒤로 감싸주면 된다. 
- 세트의 장점: 특정 항목과 다른 특정 항목의 **교집합을 쉽게 구할 수 있음**.

​	1) 교집합: 1집합`&`2집합 연산자 혹은 1집합.intersection(2집합)

​	2) 차집합: 1집합`-`2집합 연산자 혹은 1집합.difference(2집합)

​	3) 합집합: 1집합`|`2집합 연산자 혹은 1집합.union(2집합)





## 3. def

```python
import requests
import random

def pick_lotto():
        numbers=list(range(1, 46))
        numbers=random.sample(numbers, 6) #.sample(뽑아야 될 범위, 뽑을 개수)
        numbers=set(numbers) #여기까지 하면 배열만 되고 뱉어내지 못함.
        return numbers #뱉어내라.
        
my_numbers=pick_lotto() #이게 위에 있다보면, 지정되지 않은 함수라고 에러 뜸. 위에서부터 걸러짐.
real_numbers=get_lotto()
result=am_i_lucky(my_numbers, real_numbers)
```

* 특정 함수를 **정의**하는 함수. definition의 약자.

* **순서**에 영향을 받는 함수. 

* *** 함수: 뭘 리턴하거나, 뭘 입력하거나.

* 만약 다음 def 함수에 특정 회차의 번호를 가져오고 싶다면?

  ```python
  def get_lotto(num): #여기 공백이 없는 칸엔 숫자가 들어올 방을 만들어준다.
      url='https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'+str(num)
      #그냥 'num'만 쓰면 int error가 나니까, 문자열 취급을 해준다.
  
      response=requests.get(url, verify=False)
      lotto_data=response.json()
  
      real_numbers=[]
      for key, value in lotto_data.items():
          if 'drwtNo' in key:
              real_numbers.append(value)
  
      numbers.sort()
      bonus_number=lotto_data['bnusNo']
      final_dict={
          'numbers':numbers,
          'bonus':bonus_number
      }
  
      real_numbers.sort()
  
      return {final_dict}
  
  real_numbers = get_lotto(숫자) #이곳에는 알고 싶은 회차 번호를 쓴다. #arguments=args=인자.
  print(real_numbers)
  ```




## 4. sorted, .sort

```python
a = sorted([3, 2, 1])
b = [3, 2, 1].sort()

a = [1, 2, 3]
b = None
```

* sorted(): 자동 정렬. 마지막엔 return자로 정의되어 있을 것. <u>정렬된 새로운 리스트를 리턴</u>
* .sort(): 원본 파괴. <u>리스트를 새로 정렬시켜버림</u> 





## 5. return, print

```python
def function2(x):
     a = 3
     b = 5
     y = a * x + b
     print(y)    #y값을 출력한다

d = function2(10)
35
d

```

* print(): 단순히 그 값만을 출력. 예시의 경우 y는 뱉어내지만, 그것이 입력된 d를 칠 경우 아무 값도 출력되지 않는다.
* return(): 정의된 값을 출력. 예시의 경우 y뿐만 아니라, d 함수도 출력된다. **그냥 def함수에서만 print 대신에 쓰인다고 생각하면 됨(항상 그런 것은 아니지만). def문의 결론이라고 생각하면 되고, 이 문이 끝나고 난 뒤 마지막으로 출력할 때는 print를 써도 무방.**





## 6. refactoring

* 기능이나 성능이 바뀌진 않지만, data literacy를 목적으로 하는 것을 리팩토링이라고 한다.
* convention을 지키는 것





## 7. arguments, return

```python
# 인자가 있고 리턴이 있다.
# yes in, yes out
# 인자가 있고 리턴이 없다.
# yes in, no out
# 인자가 없고 리턴이 있다.
# no in, yes out
# 인자가 없고 리턴도 없다.
# no in, no out

예시)
def pick_lotto():
    numbers=random.sample(range(1, 46), 6)
    return numbers
# yes in yes out
```





## 8. def-2: am_i_lucky quiz

* def 함수를 사용해 내가 몇 등인지 알아보기

  ```python
  #내 답
  list_1=[45, 6, 10, 5, 7]
  list_2=[9, 6, 2, 5, 7]
  
  def am_i_lucky(pick, picked): #지금부터 am_i_lucky(인자1, 인자2)라는 함수를 정의하겠다.
      pick=set(list_1)  #인자1 자리에는 list_1의 집합을 넣겠다.
      picked=set(list_2)  #인자2 자리에는 list_2의 집합을 넣겠다.
      return (pick & picked)  #그리고 이 함수의 출력값은 인자1과 인자2의 교집합이 나오게.
  
  result=am_i_lucky(list_1, list_2) 
  #am_i_lucky()함수의 결과값은 다음과 같이 정리되게.
  #이 자리에는 (pick, picked)를 넣을 수가 없는 게, def 함수 안에서만 정의했으니까 바깥까지 끌고 나올 수가 없는 것(정의가 안 돼 있다고 error가 뜸)
  
  if len(result)==6: #result, 즉 am_i_lucky()함수의 개수(len)에 따라 출력값 차등 조절
      print('1등입니다')
  elif len(result)==5:
      print('2등입니다')
  elif len(result)==4:
      print('3등입니다') 
  elif len(result)==3:
      print('4등입니다')
  elif len(result)==2:
      print('5등입니다')
  elif len(result)==1:
      print('6등입니다')
      
      
      
      
      
  #선생님 답
  def am_i_lucky(pick, picked):
      match=set(pick)&set(picked)
      if len(match)==6:
          return('1등입니다') #print는 함수 안에 가능하면 안 쓰는 게 좋다고 한다.
      elif lent(match)==5:
          return('3등입니다')
      else:
          return('꽝') 
  #return문 뒤에 괄호 써도, 안 써도 상관X. return 반복ok(어차피 실행되는 return은 하나만 실행되니까 상관없다고 함)
          
  am_i_lucky([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7]) #이대로 실행하면 아무것도 출력X
  
  
  so, 
  
  result=am_i_lucky([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7])
  print(result) #print로 출력해봐야 결과값을 알 수 있음.
  
  
  
  
  
  # ROUND2
  list_1=[1, 2, 3, 4, 5, 6]
  dict_1={
      'numbers':[1, 2, 3, 4, 5, 7]
      'bonus':6
  }
  
  def am_i_lucky(pick, picked['numbers']):
      match=set(pick)&set(picked['numbers'])
      if len(match)==6:
          return('1등입니다') 
      elif lent(match)==5 and draw['bonus'] in pick:
          return('3등입니다')
      else:
          return('꽝')
  
  result=am_i_lucky(pick_lotto(), get_lotto())
  print(result)
  ```




## 9. def-3: import functions

1. def 함수를 사용해 특정 기능을 하는 함수를 정의하고 다른 파이썬 파일에 기능을 불러오는 방법

   ```python
   #1 math_functions.py라는 파일에서,
   def average(numbers):
       # result=sum(numbers)/len(numbers)
       # return result
       return sum(numbers)/len(numbers)
   
   def cube(x):
       return x*x*x
   
   
   
   #2 do_math.py라는 파일에서,
   import math_functions
   import 
   
   print('----------------------------')
   print(math_functions.cube(5))
   print(math_functions.average([10, 20, 30]))
   
   
   
   # 출력값
   평균: 80.5
   27
   ----------------------------
   125
   20.0
   
   단점: math_functions.py에서 출력한 값이 함께 나옴. 그렇다면 어떻게 해결?
       
   
   
   # Solution
   1) math_functions.py 파일에서,
   if __name__=='__main__': #이 구문을 작성하고, 
       my_score=[79, 84, 66, 93]  #이후를 if문 아래로 종속시킨다.
       print('평균:', average(my_score))
   
       print(cube(3))  
   
   
   2) do_math.py 파일에서,
   from math_functions import cube, average
   # import를 from으로 바꾸고, 그곳에서 가져올 def 함수만 import 쓰고 쉼표로 구분해 가져옴.
   
   print(cube(5))
   print(average([10, 20, 30]))
   # math_functions. 부분을 지우고 나머지 함수 부분만 쓰면 적용됨.
   ```
