# 190107 Summary

## 문자열 메소드

1. **구조: 주어.동사(목적어) 느낌**

   `.capitalize()` 

2. **대표적인 문자열 메소드 종류:**

   - .capitalize(): 앞글자를 대문자로 만들어 반환
   - .title(): '나 공백 이후 문자를 대문자로 만들어 반환
   - .upper(): 모두 대문자로 만들어 반환
   - .lower(): 모두 소문자로 만들어 반환
   - .swapcase(): 대-소문자 역으로 변경하여 반환

   -> **여기까지 원본값 변경X**

   - .join(iterable): 특정한 문자열을 글자 사이에 반환

     ex) `!.join('아파요')` > '아!파!요'

   - .replace(old, new[, count]): 바꿀 대상 글자를 새로운 글자로 바꿔 반환

     ex) `'갑분싸'.replace('싸', 'ssafy'` > '갑분ssafy'

     ex) `'aa너무 즐거워aa'.replace('a', 'ㅠ')` > 'ㅠㅠ너무 즐거워ㅠㅠ'

   - .strip(): 문자열 제거(lstrip, rstrip)

     ex) `'    recursive!\n'.strip()` > 'recursive!'

     ex) `'       ohhhhhh!\n\t'.strip()` > 'ohhhhhh!'

     ex) `'       ohhhhhh!\n\t'.lstrip()` > 'ohhhhhh!\n\t'

     ex) `'       ohhhhhh!\n\t'.rstrip()` > '       ohhhhhh!'

   - .find(n): n번째 위치 반환, 없으면 -1 반환

     ex) `'apple'.find('p')` > 1

     ex) `'apple'.find('a')` > 0

     ex) `'apple'.find('f')` > -1

   - .index(n): n번째 위치 반환, 없으면 오류

     ex) `'apple'.index('p')` > 1

     ex) `'apple'.index('p')` > 에러

   - .isdigit(): 이거 숫자인지 아닌지 참트루 반환

     ex) `'123'.isdigit()` > True

   - .split(): 문자열을 특정 단위로 나눠 반환

     ex) `'a_b_c'.split('_')` > ['a', 'b', 'c']
