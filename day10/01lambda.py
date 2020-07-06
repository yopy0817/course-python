#람다식 - 작은 익명함수
#람다식은 함수가 실행해야 할 문장이 한 문장일 경우에만 사용할 수 있음

def add(a,b) :
    return a + b


add2 = lambda a,b : a+b
print(add2)

print( add(1,2) )
print( add2(1,2) )

#람다를 통한 함수를 매개변수로 전달
def map_template(func, L = []) :
    result = []
    for i in L :
        result.append(func(i))
    return result

result = map_template(lambda x: x*2, [1,2,3,4,5])
print(result)


def filter_template(func, L=[]) :
    result = []
    for i in L :
        if func(i) : #함수의 결과가 true라면 추가
            result.append(i)
    return result

list_data = list( range(10) ) #리스트선언
result = filter_template(lambda x: x % 2 == 0, L=list_data)
print(result)

print("--------------------------------------------")
##함수의 반환
def func(a, b) :
    def func2(a, b) :
        print(a + b)

    return func2

result = func(10, 20)
result(100, 200)
##함수의 반환 - 람다식
def func(a, b) :

    return lambda a, b: print(a + b)

result = func(10, 20)
result(100, 200)