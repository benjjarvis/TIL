
def average(numbers):
    # result=sum(numbers)/len(numbers)
    # return result
    return sum(numbers)/len(numbers)

def cube(x):
    return x*x*x


if __name__=='__main__':
    # 1. 평균값을 구하시오.
    my_score=[79, 84, 66, 93]
    print('평균:', average(my_score))

    # 2. 3제곱을 하시오.
    print(cube(3))

