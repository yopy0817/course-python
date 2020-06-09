#문자포멧
#{:전체자리수.출력할문자개수}
b = "hello world"
print("{}, {:s}, {:20}, {:5} 끝".format(b,b,b,b))
print("{}, {:.5}, {:10.5} 끝".format(b,b,b))