#sort() - 정렬
numbers = [1,2,3,4,5,6,7,8,9,0]
print(numbers)
numbers.sort() #오름차순 정렬
print(numbers)
numbers.sort(reverse=True) #내림차순 정렬
print(numbers)


print("---------------------------")
#copy() - 복사한 새로운 리스트 생성
# = 를 통해 값을 복사 
numbers = [5,4,3,2,1]
new_numbers = numbers.copy()
print("복사리스트", new_numbers)
print("원본리스트", numbers)

numbers.sort()
print("복사리스트", new_numbers) #두리스트는 당연히 다르다
print("원본리스트", numbers)

print("---------------------------")
numbers = [5,4,3,2,1]
new_numbers = numbers
print("복사리스트", new_numbers) 
print("원본리스트", numbers)

numbers.sort() 
print("복사리스트", new_numbers) #두 리스트가 같다 (주소값때문..)
print("원본리스트", numbers)





