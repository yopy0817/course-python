# 함수 선언은 def 함수명(매개변수) : 로 선언합니다
# 함수의 실행 구문은 반드시 들여쓰기 처리되어야 합니다.
# 함수의 첫번째 줄에 써주는 문자열은 함수의 설명서 역할을 합니다. (docstring)
def calSum() :
    "1부터 10까지 합을 구하는 함수입니다"
    sum = 0
    for i in range(1, 11) :
        sum += i
    print("1~10까지 합:", sum)

calSum()
calSum()


