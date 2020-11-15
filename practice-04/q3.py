# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다.
# 이 프로그램의 오류를 수정해 보자.


input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

# input 의 리턴값은 문자열이다.
print(type(input1), type(input2))

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)
