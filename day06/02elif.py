'''
if문을 만족하지 않을 경우 다음 조건을 검사하고 싶다면 elif 구문을 사용합니다.
단독으로 사용할 수 없으며, 여러개 넣을 수 있습니다.
단, 만족하는 if문을 하나만 실행하게 되고 종료합니다.
'''
score = int(input("점수를 입력하세요:"))
if score >= 90 :
    if score >= 95 :
        print("A+학점 입니다.")
    else :
        print("A학점 입니다.")
        
elif score >= 80 :
    print("B학점 입니다.")
elif score >= 70 :
    print("C학점 입니다.")
elif score >= 60 :
    print("D학점 입니다.")
else :
    print("F학점 입니다.")
    print("다시 시도 하실래요?")

print("시험이 종료되었습니다")
