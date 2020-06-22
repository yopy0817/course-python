##인덱싱
number2 = [1,2, ['a', 'b', ["hi", "world"]]]
print(number2[1])
print(number2[2][1])
print(number2[2][2])
print(number2[2][2][1])

print("---------------------------------------")
##슬라이싱 #number2[from : to] -마지막은 포함하지 않음
number2 = [1,2,3,4,5,6,7,8,9,0 ]
print( number2)
print( number2[1 : 3]) 
print( number2[0 : 5]) 

print("---------------------------------------")
##슬라이싱 #number2[from : to : by] from부터 to까지 by번재 항목 추출
print( number2[0:10:2])
print( number2[2:7])
print( number2[2:7:1])

print( number2[ : :2])
print( number2[ : :-1]) #거꾸로
print( number2[ : :-2])
print( number2[-5: : -1]) #거꾸로

print("----------------------")
##인덱싱을 통한 값 수정
numbers = [1,2,3,4,5,6,7,8,9,0]
number2[0] = 100
number2[1] = 200
print(number2)
number2[0:5] = [10, 20, 30] # 0~5까지 매 인덱스를 10,20,30으로 변경
print(number2)
number2[0:5:2] = [100, 200, 300] #0~5까지 2번째 마다 100, 200, 300으로 변경
print(number2)
#number2[0:10:2] = [1,2,3]  #값의 개수가 맞지 않다면 에러 발생

