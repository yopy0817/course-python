#break는 가장 가까운 중첩구문을 빠져나옵니다.
for i in range(0, 10) :
    if i == 5 :
        break
    print(i, end=" ")
print()

print("-----------------")
#중첩 구문에서는 안쪽 반복문을 빠져나옵니다.
for i in range(0, 3) :
    for j in range(0, 3) :
        if i == j :
            break
        print("{}-{}".format(i,j))

print("-----------------")
#중첩 구문에서 바깥 반복문 까지 종료 하고 싶다면 변수를 사용합니다.
flag = False
for i in range(0, 10) :
    for j in range(0, 10) :
        if j == 5 :
            flag = True
            break
        print("{}-{}".format(i,j))

    if flag :
        break
