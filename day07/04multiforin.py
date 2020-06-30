#모든 구구단 출력
for i in range(2, 10) :
    for j in range(1, 10) :
        print("{}x{}={:>2}".format(i, j, i*j), end=" ")
    print()



print("--------------")
# 2차원 데이터를 다룰 때도 사용할 수 있다.
list_2d = [[1,2,3,4,5], [11,12,13,14,15], [21,22,23,24,25]]

for data in list_2d :
    print(data)

print("--------------")
# 전부 처리하려면?
for row in list_2d :
    for data in row :
        print(data, end=" ") #가로출력
    print() #줄바꿈


print("--------------")
## 다차원 리스트 전부 출력
list_3d = [
    [[1,2,3,4,5],
     [11,12,13,14,15],
     [21,22,23,24,25]],
    [[6,7,8,9,10],
     [16,17,18,19,20],
     [26,27,28,29,30]]
]

for face in list_3d :
    for row in face :
        for data in row :
            print(data, end=" ")



