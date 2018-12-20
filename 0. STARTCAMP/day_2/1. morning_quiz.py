#평균을 구하시오. type로 float가 나와야 한다.
my_score=[79, 84, 66, 93]
my_average=sum(my_score)/len(my_score)

print(my_average)
type(my_average)


your_score={
    '수학':87,
    '국어':83,
    '영어':76,
    '도덕':100
}

your_average=sum(your_score.values())/len(your_score)
# a=your_score['수학']+your_score['국어']+your_score['영어']+your_score['도덕']
# b=len(your_score)
# your_average=a/b

print(your_average)
type(your_average)