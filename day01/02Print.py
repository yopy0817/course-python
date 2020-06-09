# 파이선의 출력과 서식문자 \t \n print()
# 문자와 숫자
print("1") #문자
print('1') #문자
print(1)
# 문자열을 더했을 때 문자열을 붙인 형태가 됩니다.
# print("1" + 1) 숫자와 문자를 더하면 에러가 발생합니다
print("1" + "1")
print("1" + '1')
print(1 + 1)


# 한줄에 여러개를 출력하고 싶다면? ,로 구분합니다
print("안녕", "하세요.", "반갑습니다")

# sep은 출력문의 구분자를 지정합니다
print("hello", "world", sep=" ") #기본값
print("hello", "world", sep="")
print("apple", "banana", "melon", sep=",")
print("apple", "banana", "melon", sep="\t")

# end는 출력 후 줄바꿈 문자를 지정합니다
print("오늘은 날씨가 맑습니다.", end="\n") #기본값
print("공부하기 좋은 날씨네!", end=" ") 
print("아 좋다 좋아~")










