# 함수의 반환 return

#매개 변수로 전달 받은 2개의 값의 합을 반환하는 함수.
def add(a, b) :
    return a + b

result = add(10, 20)
print("10과 20의 합:", result)

#매개변수 까지의 합을 반환하는 함수.
def calSum(a) :
    sum = 0
    a = 1
    while a <= 10 :
        sum += a
        a = a + 1
    return sum

result = calSum(10)
print("1부터 10까지 합:", result)

#리스트의 반환
def func(a) :
    "a까지 3의 배수만 리스트에 저장하고 반환"
    result = []
    i = 1
    while i <= a :
        if i % 3 == 0 :
            result.append(i)
        i = i + 1
        
    return result    

result = func(20)
print("20까지의 3의 배수:", result)

