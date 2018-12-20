cities_temp={
    '서울': [-6, -10, -5],
    '대전': [-3, -5, 2],
    '광주': [0, -5, 10],
    '구미': [2, -2, 9]
}


#도시별 온도 평균
#서울: ?
#대전: ?
#광주: ?
#구미: ?

for city,temperatures in cities_temp.items():
    print(city+': '+str(round(sum(temperatures)/len(temperatures), 2)))



#도시중에 최근 3일간 가장 추웠던 곳과 가장 더웠던 곳은?
#Hottest: ??, Coldest: ??

# for city in cities_temp:
# 		temperatures=cities_temp[city]
# 		temperatures.index(max(cities_temp[city]))
#         if temperatures.index(max(cities_temp[city]))=temperatures.find()


all_temp=[]
for key, value in cities_temp.items():
    all_temp+=value
    
print(all_temp)

hottest=max(all_temp)
coldest=min(all_temp)

for key, value in cities_temp.items():
    if hottest in value:
        print('Hottest: ', key)
    if coldest in value:
        print('Coldest: ', key)