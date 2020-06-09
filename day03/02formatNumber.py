#숫자포멧
#공백은 그대로 출력, :10은 남은 자리수 만큼의 공백 지정, 자리수가 짧으면 길이만큼 출력됩니다.
a = 12345
print("{}, {:10}, {:3}".format(a,a,a)) #지정된 자리수를 넘어가면 전부 출력합니다.
""" 
:d 정수
:f 실수
:b 2진수
:o 8진수
:x 16진수
실수의 경우 소수점 6자리까지 표기
"""
print("{:d}, {:f}, {:b}, {:o}, {:x}".format(a,a,a,a,a))

#소수점의 자리수 지정{:전체자리수.소수점자리수f} -소수점 포함
print("{}, {:f}, {:15f}, {:10.2f}, {:20.10f}".format(a,a,a,a,a))