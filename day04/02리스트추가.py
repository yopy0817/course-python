#2차원 리스트
numbers = [1,2,3,4,5]
number_2d = [[1,2,3,4,5], [10,20,30,40,50], [2,4,6,8,10] , [1,3,5,7,9] ]

print(numbers)
print(number_2d)

print("길이:" ,  len(numbers) )
print("최대값:" ,  max(numbers) )
print("최소값:" ,  min(numbers) )

print( max(number_2d )) #첫번째 항목이 가장큰값을 반환

#리스트를 합치거나 곱하면 추가한만큼 더해집니다.
new_list = numbers * 3 + numbers
print(new_list)


#리스트에 끝에 추가하는 함수 append()
numbers.append(100) #100 추가
print(numbers)
numbers.append([10,20,30,40,50])
print(numbers) #2차원 형태로 추가가 됨

#리스트끝에 리스트의 요소를 순서대로 추가 extend(리스트)

#리스트에 중간에 추가 insert(인덱스, 값)

#값의 개수를 찾아주는 함수 count(찾을값)

#값을 index기반으로 찾는 함수 index(찾을값)
#값을 index기반으로 찾는 함수 index(찾을값, 이후에 찾을값)
numbers = [1,2,3,4,5, 1,2,3,4,5]
print( numbers.index(3) ) #2번 index에 있습니다
print( numbers.index(3, 5) ) #7번 index에 있습니다
