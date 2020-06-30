'''
while문

'''
# while문 기본
i = 1
while i <= 10 :
    print(i, end = " ")
    i = i + 1

print()

# 짝수 출력
i = 1
while i <= 10 :
    if i % 2 == 0 :
        print(i)
    i+=1
