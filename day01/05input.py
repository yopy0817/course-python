#그렇다면, 정수를 입력받고 싶으면 어떻게 해야하는가? int(값) 함수를 이용합니다.
""" 
print("두 정수를 입력하세요>")
print("정수1>", end="")
num1 = input()
print("정수2>", end="")
num2 = input()

print( int(num1) + int(num2) )
"""

print("두 정수를 입력하세요>")
print("정수1>", end="")
num1 = int(input()) 
print("정수2>", end="")
num2 = int(input())

print(num1 + num2)
