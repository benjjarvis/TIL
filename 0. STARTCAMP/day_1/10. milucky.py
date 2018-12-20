import requests
import random


url='https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response=requests.get(url, verify=False)
lotto_data=response.json()


real_numbers=[]

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
print(real_numbers)



#1등: my_numbers==real_numbers
#2등: real_numbers & my_numbers 5개 같고, 나머지 하나의 my_numbers==bonus number
#3등: real_numbers & my_numbers 5개 같다.


my_numbers=[1, 2, 3, 4, 5, 6]
real_numbers=[1, 2, 3, 4, 5, 6]
bonus_number=7

count=0
for my_number in my_numbers:
	for real_number in real_numbers: 
                if my_number==real_number:
                        count+=1
print(count)

if count==6:
    print('1등')
elif count==5 and bonus in my_numbers:
    print('2등')
elif count==5:
    print('3등')
