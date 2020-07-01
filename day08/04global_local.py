# 전역변수와 지역변수
# 함수 밖에서 만들어진 변수는 함수 안에서 사용이 가능합니다.
a = "홍길자"
def func1() :
    print(a)

def func2() :
    print(a)    

func1()
func2()

# 반대로 함수 안에서 선언된 변수는 함수 안에서만 사용할 수 있습니다.
def func3() :
    b = 10
    print(b)

func3()
# print(b) 

print("-----------------------------------")
# Lexical scope - 
# 함수가 전역변수와 동일한 지역변수를 가지고 있을 때
# 함수안에서 전역변수를 참조하지 못하는 특징을 갖는데 Lexical특성 이라고합니다.

c = 10
def func4() :
    print("before", c)
    # c = 100 #에러! before출력문이 지역변수를 참조하는 문제
    print("after", c)

func4()

d = 100
def func5() :
    #전역변수를 사용하고 싶다면, 변수 사용 전에 global키워드를 이용해서 선언하면 됩니다
    global d
    print("before", d) 
    d = 200
    print("after", d)

func5()

## 함수 이름 변경
## 파이선은 함수자체를 변수에 저장하는 문법을 허용합니다
def func6(n) :
    sum = 0
    a = 1
    while a <= n :
        sum += a
        a = a + 1 
    print("1부터 n까지합:", sum)    
func6(10)

function = func6 # 함수를 변수에 저장
function(10)


