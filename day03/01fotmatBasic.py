name = "홍길동"
age = 20

print(name, "님의 나이는", age, "세 입니다.")
print(name, "님의 나이는", age, "세 입니다.", sep="")

#변수와 텍스트를 번걸아 사용하면, 가독성이 떨어지고 코드작성이 어렵다.
#포멧기능을 사용합니다.
#포멧의 순서의 지정이 가능합니다.  (인덱스 시작은 0부터)
print("{}님의 나이는 {}세 입니다".format(name, age))
print("{1}님의 나이는 {0}세 입니다".format(age, name))
print("오늘은 {}년 {}월 {}일 입니다".format(2020, 1, 1))





