#튜플은 읽기전용, 속도가 빠르다 () 를 이용한다
numbers = (1,2,3,4,5)
print(type(numbers))

#튜플은 한개만은 저장할 수 없다
numbers = (1) # 안됨
numbers = (1, ) # 됨

numbers = (1,2,3,4,5)
#길이확인 - len(튜플명)

#작은값 - min(튜플명)

#큰값 - max(튜플명)

#값의 개수 확인 - count(값)

#값이 들어있는 위치 - index(값)
numbers = (1,2,3,4,5,1,2,3)
numbers.index(3, 5) #3의 값을 5인덱스 뒤에서 찾는다
print("5번째 뒤에 3의 위치:", numbers.index(3, 5) )


#튜플도 1차원 2차원 3차원이 가능합니다.
data = (1,2,3,4, (5,6,7,8))
print(data)

#튜플의 인덱싱
numbers = (1,2,3,4,5,6,7,8,9,0)
print("2~8인덱스의값:", numbers[2:8])
print("-5~-2인덱스의값:", numbers[-5:-2])

#튜플의 슬라이싱
print("0~5까지 매2씩 확인:", numbers[0:5:2])
print("거꾸로:", numbers[::-1] )

#튜플은 읽기전용 이기 때문에, 요소의 추가 삭제 함수가 불가능하다
# numbers.append(6) #에러
# numbers.insert(1, 6) #에러
# numbers[0] = 6 #에러
# numbers.remove(3) #에러












