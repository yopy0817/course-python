# 매개변수란 함수의 전달되는 값을 의미합니다.
def add(a, b) :
    print("{}와 {}의 합은 {}".format(a, b, a+b))

add(20, 3)



''' 수정중.....
def fiboancci(n) :
    "피보나치 함수...."
    a, b = 0, 1
    while a < n :
        print(a, end=" ")
        # a = b
        # b = a + b
        a, b = b, a+b 

fiboancci(10)
'''