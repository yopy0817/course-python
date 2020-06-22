# pop() 은 마지막 값을 출력하고 삭제
# pop(index) 는 index번째를 삭제
numbers = [1,2,3,4,5,6,7,8,9,0]
numbers.pop()
print(numbers)
numbers.pop(5) #5번재 인덱스 삭제 
print(numbers)

print("--------------------------")
# remove(값) - 해당 항목 삭제
numbers = [1,2,3,4,5,6,7,8,9,0]
numbers.remove(5)
print(numbers)
#numbers.remove(100) #지울값이 없다면 에러 발생

print("--------------------------")
# clear() - 리스트의 요소를 전부삭제
numbers.clear()
print(numbers)