'''
나열된 자료를 하나씩 빼내서 저장할 변수 또는 변수의 목록입니다
'''
for i in [0,1,2,3,4,5,6,7,8,9] :
    print(i, end=" ")
print()

for i in range(0, 10) : #range(10) :
    print(i, end=" ")
print()

#리스트에 적용
list1 = ["홍길동", "홍길자", "이순신"]
for i in list1 :
    # print(i)
    print("{} 입니다".format(i))

#딕셔너리에 적용
color = {"apple": "red", "banana": "yellow", "grape": "pupple"}
for i in color :
    # print(i) #키를 뽑는다
    print(color.get(i))
print()
#딕셔너리의 값을 뽑는다
for i in color.values() :
    print(i)
print()
#딕셔너리를 튜플로 변경해서 키와 값을 뽑는다
for k, v in color.items() :
    print("키:" + k, "값:" + v)
