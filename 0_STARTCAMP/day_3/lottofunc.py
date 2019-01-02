# my_numbers=pick_lotto()
# real_numbers=get_lotto()
# result=am_i_lucky(my_numbers, real_numbers)

import requests
import random


def pick_lotto():
    numbers=list(range(1, 46))
    numbers=random.sample(numbers, 6)
    return numbers

my_numbers=pick_lotto()
print(my_numbers)


def get_lotto():
    url='https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

    response=requests.get(url, verify=False)
    lotto_data=response.json()

    real_numbers=[]
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            real_numbers.append(value)

    real_numbers.sort()
    bonus_number=lotto_data['bnusNo']
    final_dict={
        'numbers':numbers,
        'bonus':bonus_number
    }

    real_numbers.sort()

    return {final_dict}

real_numbers = get_lotto()
print(real_numbers)


#결과값 
# [1, 2, 3, 4, 5, 6]
# [[1, 2, 3, 4, 5, 6], 7]
# {numbers:[1, 2 ,3, 4, 5, 6], bonus:7}
