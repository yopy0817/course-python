#  set은 순서가가 없고 중복을 허용하지 않습니다. {} 로 생성합니다.
fruits = {'apple', 'orange', 'banana', 'apple'}
print(fruits)

# set()함수를 이용해서 리스트나 튜플을 set으로 변경이 가능합니다.
s1 = set([1,2,3])
s2 = set((1,2,3))
s3 = set({"number": 20})

print(s1, s2, s3)

#set의 항목추가 add() - 튜플을 추가, update() - 리스트, 딕셔너리 추가
fruits.add("mango")
print( fruits )
fruits.add( (1,2) )
print( fruits )
# fruits.add([1,2,3]) #에러
# fruits.add({1,2,3}) #에러
fruits.update( [3,4] ) 
fruits.update( {True, False} )
print( fruits )


#set의 항목삭제 remove(값)
fruits.remove( (1,2) )
fruits.remove( 3 )
fruits.remove( 4 )
print(fruits)
#논리값 True, False는 1,0 으로 삭제가 가능합니다
fruits.remove( 1 )
fruits.remove( 0 )
print(fruits)

