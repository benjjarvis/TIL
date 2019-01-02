
# 인자가 있고 리턴이 있다.
# yes in, yes out
# 인자가 있고 리턴이 없다.
# yes in, no out
# 인자가 없고 리턴이 있다.
# no in, yes out
# 인자가 없고 리턴도 없다.
# no in, no out

# def pick_lotto():
#     numbers=random.sample(range(1, 46), 6)
#     return numbers
# yes in yes out




# my_numbers = pick_lotto()
# real_numbers = get_lotto(837)
# result = am_i_lucky(my_numbers, real_numbers)

# print(result)

# print(am_i_lucky(my_numbers, real_numbers))
# 1등


# 외부 로또번호 API
# import requests

# def get_lotto(num):
# 	url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(num)
# 	response=requests.get(url)
# 	lotto_data=response.json

# real_numbers=[]
# for key, value in lotto_data.items():
# 	if 'drwtNo' in key:
# 		real_numbers.append(value)
# 		real_numbers.sort()

#     return real_numbers









# 내 당첨결과 알아보는 코드
list_1=[45, 6, 10, 5, 7]
list_2=[9, 6, 2, 5, 7]

def am_i_lucky(pick, picked):
    pick=set(list_1)
    picked=set(list_2)
    return (pick & picked)

result=am_i_lucky(list_1, list_2)

    
if len(result)==6:
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