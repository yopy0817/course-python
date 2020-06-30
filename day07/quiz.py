## 1부터 30까지 자연수 중의 3의 배수의 총합을 출력하는 코드
sum = 0
for i in range(0, 31) :
    if i % 3 == 0 :
        sum = sum + i

print("1-30까지합:", sum, sep="")

## 1- 10까지 자연수 중의 홀수만 출력하는 코드
num = 0
while num <= 10:
    if num % 2 == 1:
        print(num, end=' ')
    num += 1
