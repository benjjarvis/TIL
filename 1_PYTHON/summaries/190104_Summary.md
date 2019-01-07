# 190104 Summary

## 1. Quiz

#### 1. 조건문 성질

```python
# 다음 출력될 값은?
if True:
    if False:
        print(1)
        print(2)
    else:
        print(3)
else:
    print(4)
print(5)


# 3, 5 
```



#### 2. 택시를 타는가,  뚜벅이로 가는가

```python
def is_taxi(money, card_availability):
    if money >= 4000 or card_availability:
        return('택시를 허락하노라')
    else:
        return('걸어가라')
    
print(is_taxi(2000, False))


def is_taxi(money, card_availability):
    return '택시를 허락하노라' if money >= 4000 or card_availability else '걸어가라'

print(is_taxi(2000, True))
```



#### 3. 정수 3개가 들어온다. 이때, 2번째로 큰 정수를 출력하는 코드는?

```python
# 다시 리뷰할 것
def snd_number(*nums):
    biggest = nums[0]
    rest = []
    for implicit_num in nums:
        if implicit_num > biggest:
            biggest = implicit_num
        elif implicit_num <= biggest:
            rest.append(implicit_num)
            second = rest[0]
            for implicit_two in rest:
                if implicit_two > second:
                    second = implicit_two
    return second


print(snd_number(10, 3, 4))
print(snd_number(0, -1, 2))


# 3개일 경우 한정
def second_number(a, b, c):
    # a가 middle
    if (b <= a and a <= c) or (c <= a and a <= b):
        return a
    # b가 middle
    # elif (a <= b and b <= c) or (c <=b and b <= a):
    #     return b
    elif (a <= b <= c) or (c <= b <= a):
        return b
    # c가 middle
    else:
        return c
```



#### 4. 환율 계산

```python
# input -> 100 달러, 300 유로, 200 위안, 1000 엔
# 1
msg1, msg2 = input('값을 입력하세요: ').split(' ')

volume = int(msg1)
unit = msg2

def cur_cal(volume, unit):
    if unit == "달러":
        return currency['USD'] * volume 
    elif unit == "엔":
        return currency['JPY'] * volume
    elif unit == "유로":
        return currency['EUR'] * volume
    else:
        return currency['CNY'] * volume

print(enumerate(cur_cal), str(unit))



# 2
def currency_calculator(volume, unit):
    currency = {
    'USD': 1167,
    'JPY': 1.096,
    'EUR': 1268,
    'CNY': 171
    }

    if unit == "달러":
        key = 'USD'
    elif unit == "엔":
        key = 'JPY'
    elif unit == "유로":
        key = 'EUR'
    elif unit == "위안":
        key = 'CNY'
    else:
        print('error')

    return volume * currency[key]

print(currency_calculator(10, '엔'))



# 3
def currency_calculator(volume, unit):
    currency = {
    'USD': 1167,
    'JPY': 1.096,
    'EUR': 1268,
    'CNY': 171
    }

    unit_currency = {
        '달러': 'USD',
        '엔': 'JPY',
        '유로': 'EUR',
        '위안': 'CNY'
    }
    
    return volume * currency[unit_currency[unit], 2]
```



#### 5. 시그마

```python
def sigma(n):
    return sum(range(1, n+1))
```



#### 6. 구구단

```python
for a in range(1, 10, 1):	# 1씩 증가하며 나열해라
    for b in range(1, 10, 1):
        print(a * b, end='  ')
    print()  # 이걸 다시 출력하는 이유는, 한 바퀴 돌리고 엔터치는 느낌이라서?
```



#### 7. 크리스마스 트리

```python
h = 5

# for문 한줄짜리
print(' '*(h-1), '☆')
for i in range(h):
    print(' '*(h-i-1), '*'*((i+1)*2-1), ' '*(h-i-1))
    
    
# for문 두줄짜리
for i in range(h):
	for j in reversed(range(h)):
		if i < j:
			print(' ', end='')
		else:
			print('*', end='')
	for j in range(h):
		if i > j:
			print('*', end='')
	print()
```



#### 8. 리스트 특정 값만 삭제

```python
colors = ['red', 'green', 'blue', 'white', 'black', 'gold']

certain_num = colors[0], colors[4], colors[5]
color_del = set(colors) - set(certain_num)


print(list(color_del))
```



#### 9. 달력 만들기

```
이건 숙제
```





## 2. OS & CLI(Command Line Interface)

![](C:\Users\student\Downloads\다운로드.png)

1. git bash: 윈도우 운영체제에서 유닉스 운영체제의 커맨드 라인을 사용할 수 있도록 고안된 프로그램. 
   - pwd: present working directory.
2. ls: list. 지금 내 현재 위치의 폴더 리스트를 뽑아줘라.
   * ls -a: ls --all. 현재 있는 위치의 숨겨진 폴더 리스트까지 다 보여줘라.
   * ls -l: long. 길게 보여줘. + 메모리도 보여줌(ls -lh라 쓰면 인간이 알아볼 수 있는 메모리로 환산)
   * ls -al: all, long. 모두 길게 보여줘.
   * 왜냐하면 유닉스에서는 '.laskd'에서 .이 숨겨져 있다는 의미이기 때문에.
   * ls a: 파일명이 a인 파일을 리스팅해줌.
   * ls a*: a로 시작하는 모든 파일을 리스팅해줌.
3. /: '내 PC'
4. cd: change directory. 특정 디렉토리로 이동해라.
5. mkdir: make directory. 새로운 디렉토리(폴더)를 생성해라.
   - mrdir -p ssafy/ss3/students: ssafy라는 폴더를 생성하고, 거기에 ss3를 생성하고, students를 생성하라.
   - 이때 -p는 여러 단계에 걸쳐 폴더를 생성하기 귀찮으니까 한번에 처리해 버리겠다는 명령어.
6. touch: make a file. 새로운 파일을 생성해라.
   - touch a.txt b.txt c.txt d.py 등 공백으로 구분함.
   - touch .hidden: hidden이란 이름의 숨김 파일(확장자X)을 생성해줘.

7. vim: visual edit improved(추정). touch로 생성한 파일을 vim + 파일명 입력하면 텍스트 파일이나 파이썬 문서를 cmd mode에서 쓸 수 있음.
   - ex) vim classmates.txt를 입력하면
   - 정말 메모장처럼 쓸 수 있고, 엔터는 shift + enter, 저장은 :w, 나가기는 :q
8. $: prompt. 즉시 명령어를 실행해라(컴퓨터 입장에서는 실행할 준비가 됐어).
9. ^C: Ctrl + C. 정식 명칭은 'carrot'. 취소하는 키.
10. echo: print()와 같은 키. 유닉스에서는 echo로 통일. 풀네임은 'echo standard out'
    - echo hello를 치든가, echo 'goodbye'를 치든가.
    - echo "When I was a young girl" > black_parade.txt : black_parade.txt라는 파일에 "When I was a young girl"이란 말을 써라! 라고 직관적으로 명령어.
    - ' > ' : redirect symbol. 덮어씌우는 키.
    - ' >> ' : append symbol. 추가하는 키.
11. cat: 안의 내용물을 출력하는 키. 
    - cat black_parade.txt : "When I was a young girl"가 출력됨.
12. man: manual. help()와 같은 키.
    - man echo를 치면 echo에 관한 매뉴얼들이 주르륵 나옴.
13. Ctrl + p: previous. 이전에 입력했던 명령어가 나옴.
14. clear: 화면을 쭉 밀어버리는 것(그렇다고 명령어 다 삭제되는 거 아님).
15. Ctrl + l: 아예 새롭게 밀어버리는 것. 
16. Ctrl + d: destroy. 터미널을 날려버리거나 파이썬 프로그램에 들어갔을 때 꺼버리는 키.
17. python: 입력하면 파이썬 프로그램이 실행됨.



**echo를 쓰지 않고, line_1.txt와 line_2.txt에 저장한 가사들을 song.txt에 넣기**

```bash
benjjarvis:~/workspace $ cat line_1.txt > song.txt
benjjarvis:~/workspace $ cat line_2.txt >> song.txt
benjjarvis:~/workspace $ cat song.txt
Thought I'd end up with Sean
But he wasn't match
```



**line_2.txt와 line_1.txt에 저장한 가사들을(거꾸로 순서대로) reverse.txt에 넣기**

```bash
benjjarvis:~/workspace $ cat line_2.txt line_1.txt >> reverse.txt
benjjarvis:~/workspace $ cat reverse.txt
But he wasn't a match
Thought I'd end up with Sean
```



18. mv: move. 파일명 변경.
    - 예: mv reverse.txt rev.txt 
19. cp: copy. 특정 파일의 내용을 복사하기.
    - 예: cp rev.txt copy.txt
20. rm: remove. 파일 지우기
    - 예: rm. hidden
    - rm -i rev.txt: '정말 지울거니?(remove regular file 'rev.txt'?)'라고 다시 한번 물어봄. 나만 사용할 땐 상관없는데, 타인에게 가이드하기 위해서는 필요할 수도 있음. 그리고 그냥 쓰면 완전히 삭제해버리기 때문에 위험할 수도 있어서, i를 사이에 넣어주는 게 좋음.
    - rm -f rev.txt: 사실상 그냥 rm과 차이가 없어보이지만, 더 위험한 명령어.
      - -f: force. 강제로 실행. == --force.
    - rm *.txt: txt라는 확장자를 가지고 있는 파일을 모두 삭제(asterisk = wildcard = all).
       - a* : a로 시작하는 파일 다 지우기
       - asterisk(solo): 그냥 모든 파일 다 지우기
21. which 파일명: 특정 파일이 있는지 위치를 뱉어주는 기능.



**특정 html 파일을 배쉬에 끌어오기**

```bash
curl -OL neovansoarer.github.io/files/sonnets.txt
```

22. curl: 지정한 url로 가서 그 안의 html 파일을 가져와라.

    - curl -L: location
    - curl -O: remote name

23. head: 특정 텍스트 파일의 앞부분 10줄만 보여줌.

    - 예: head sonnets.txt 

24. tail: 특정 텍스트 파일의 뒷부분 10줄만 보여줌. 쌓인 로그 수정할 때 많이 사용한다고 한다.

    - 예: tail sonnets.txt

25. ping: 특정 페이지가 잘 돌아가는지 시스템을 확인.

    - 예: ping google.com

26. wc: word count. 글자수 세는 기능.

    - 예: wc sonnets.txt -> 줄, 단어, 글자 순으로 배출.
    - | wc: 파이프 앞에 있는 표준 출력을 그대로 뒤의 명령어에 적용시키는 명령어. 그래서 stream이라고도 함. 흐름을 넘기는 명령어라고 해서.
      - head sonnets.txt | wc

27. less: 리더기를 켜라. 나올 때는 q(quit)로. 검색되고 편집은 안 됨.

    - 예: less sonnets.txt
    - /키워드: 키워드를 검색함.
      - n: next page
      - shift + n: next keyword

28. grep: globally regular expression. 특정 키워드를 특정 문서에서 찾는 기능. 그냥 'grap'처럼 이해하면 될 듯?

    - 예: grep rose sonnets. txt

    - grep -i rose sonnets.txt: case insensitive. 대소문자 상관없이 소네트에서 rose를 찾겠다.

29. ps aux: 돌고 있는 프로세서들을 다 알려주는 기능. processor auxiliary?

    - ps aux | grep jupyter를 치면 돌아가고 있는 시스템에서 jupyter를 찾아줌.

30. top: 컴퓨터에서 리소스를 제일 많이 잡아먹고 있는 프로세스를 보여줌. 나갈 때는 q. 

31. /: 디렉토리 최상단. root directory. 거의 태초신 같은 느낌. 접근하면 망할 확률 99.999999%. 그래서 컴퓨터 자체 내에서 접근 권한을 제한해놨음. 여기까진 거의 못 감. 

    - 구조: test/일 경우에 test라는 이름의 디렉토리.

    - touch /opt/fake_file: 최상단 디렉토리에 opt/가 분명히 있지만, 여기서 파일을 만들 수 없음.

32. sudo: super user do. 사용자에 권한을 최대로 부여하고 명령어를 이행하는 방법. 

    - 이걸로 만들면, 일반 rm이나 rm -f로도 지워지지 않아서 sudo를 앞에 데리고 지워야 함.

33. ~: 디렉토리 주소에서 물결 표시(~)는 home을 의미. 이때 home은 단순한 바탕화면을 의미하는 게 아니라, 그냥 내가 위치한 디렉토리 내부를 의미하는 것 같음. 약간 workspace, working ground / playing ground 같은 느낌?

    - 근데 보통 cd만 쳐도 cd라는 홈 그라운드로 자동으로 이동. 

34. rmdir: 디렉토리 삭제. 

    - but 비어있지 않은 디렉토리는 이 명령어로 삭제할 수 없음.
    - rmdir -f / rm -r(recursive): 디렉토리, 어쨌거나 지워버리는 명령어.
    - rm -rf: 파일과 폴더를 강압적으로 지우는 명령어.
    - sudo rm -rf /: 컴퓨터 그냥 날려버리겠다는 의미. 

35. '..': 계층 한 단계 위로 이동.
    - 예: cd ../../ : 두 계층 위로 이동.
36. '.': 제자리에서 점프? '지금 내가 있는 것 모두 다'라는 의미.
    - add . : 지금 내 위치에 있는 파일/폴더 다.
37. cd -: 뒤로가기.