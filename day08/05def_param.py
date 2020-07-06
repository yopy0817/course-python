# 다양한 매개변수
# 매개변수가 기본값을 가질 때 - 기본값이 있는 매개변수는 선택적으로 사용이 가능합니다.
# 단 기본값이 있는 매개변수는 반드시 뒤쪽에 작성합니다.
def make(age, name="홍길동") :
    print("나이는 {} 이름은 {} ".format(age, name) )

make(20)
make(20, "이순신")
make(30, "홍길자")

# 매개변수의 기본값이 변수일 경우 - 함수가 정의되는 시점의 값이 사용됩니다.
i = 10
def func1(arg=i) :
    print(arg)

i = 100
func1()

print("-------------------------------------")
# 매개변수의 값이 리스트일 경우
list_ = []
def func2(a, L = list_) :
    L.append(a)

func2(1)
func2(2)
print(list_)
print("-------------------------------------")
# 매개변수의 선택적 처리
def func3(a, L=None) :
    if L == None :
        L = []
    L.append(a)
    print(L)

func3(1)
func3(2)
func3(3, list_)
print("-------------------------------------")
# 키워드 인수는: 함수 호출 시 인수가 매개변수의 이름을 갖는 것
list_ = []
def func4(a, L=list_) :
    L.append(a)
    print(L)

func4(10, L = list_) #가능
func4(a = 10, L = list_) #가능
func4(L = list_, a = 10) #가능
#func4(50, a = 10) #에러 - 값이 없는 인자값이 기본 인수에 먼저 할당되기 때문입니다.
#func4(L = list_, 10) #에러 - 매개변수를 갖지 않는 인수가 무조건 먼저 나와야 합니다.

print("-------------------------------------")
# 튜플매개변수 *args 가변인수 - 함수의 전달하는 인자값이 튜플로 처리됩니다 
def add(*args) :
    print(args)

    sum = 0
    for i in args :
        sum += i
    print("결과:", sum, sep="")

add(1,2,3)
add(1,2,3,4)
add(1,2,3,4,5,6,7)

print("-------------------------------------")
# 인수의 전달 순서: 순서인수, 튜플인수, 키워드인수
def concat(*args, sep) :
    result = sep.join(args) #join은 문자열 더하기 기능
    print( result ) 

# concat("apple", "banana", "grape", ",") #에러 - sep에 전달되는 값이 없기 때문
concat("apple", "banana", "grape", sep="/")

print("-------------------------------------")
# 딕셔너리 매개변수 **args 가변인수 : 함수의 전달되는 값이 딕셔너리로 처리됩니다.
def func5(a, *b, **c) :
    print(a)
    print(b)
    print(c)

func5(10, 1,2,3,4,5, name="길동", age=20)
## 매개변수와 인수의 순서: 순서인수, 튜플인수, 키워드인수, 딕셔너리인수



print("-------------------------------------")
## 튜플인수 언패킹: 함수 호출시 튜플 변수 앞에 *
## 딕셔너리 인수 언패킹: 함수 호출시 딕셔너리 변수 앞에 **
def func6(*data) :
    sum = 0
    for i in data :
        sum += i
    print("결과:", sum, sep="")

numbers = (1,2,3)
func6(1,2,3)
# func6(numbers) #에러: ((1,2,3,4,5)) 이런형식이 되기 때문이다
func6(*numbers) #언패킹

def func7(**data) :
    for i in data.items() :
        print(i)

info = {"age": 20, "name": "홍길동"}
func7(age = 20, name="홍길동")
# func7(info) #에러: ?? = {"age": 20, "name": "홍길동"} 이런형식이 되기 때문
func7(**info) #언패킹



