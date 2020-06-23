# 딕셔너리는 키와 값의 쌍으로 구성된 형태 {}로 선언합니다
# 딕셔너리의 키값은 유일하며, 값을 중복이 가능합니다

dic1 = {"name": "홍길동", "num": "10", "age": 20}
print( type(dic1) )
print( dic1 )
#딕셔너리의 사용 get(키), 대괄호
print("키가 name인값:" , dic1.get("name"))
print("키가 num인값:", dic1.get("num"))

dic2 = {1:"홍길자", 2:"이순신", 3:"홍길동"}
print(dic2)
print("키가 1인값:", dic2.get(1) )
print("키가 1인값:", dic2[1])

#딕셔너리는 동일 키를 허용하지 않습니다.
dic3 = {1: "홍길동", 1: "홍길순"}
print(dic3)
dic3 = {1: "홍길동", True: "홍길순"} #안됨
print(dic3)

#딕셔너리의 값의 추가
dic1 = {"name": "홍길동", "num": "10", "age": 20}
dic1["address"] = "서울시"
print(dic1)

#딕셔너리의 값의 수정 -동일한 키에 저장하면 값을 추가하지 않고 수정합니다.
dic1["address"] = "경기도"
print(dic1)

#딕셔너리의 값의 삭제
del dic1["address"]
print(dic1)
dic1.pop("age")
print(dic1)

#딕셔너리의 복사 cope(), =

#딕셔너리 items() - 키, 값을 튜플로 묶어서 리스트로 반환해줍니다
print(  dic1.items() )

#딕셔너리의 in 연산자는 값의 여부를 확인해서 true, false로 반환합니다
print( "age" in dic1 )
print( "address" in dic1)