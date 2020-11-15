# 이 프로그램은 우리가 예상한 "Life is too short"라는
# 문장을 출력하지 않는다
# 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.


f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()  # 열린 파일 객체를 닫아야 다음 문장이 정상수행

f2 = open("test.txt", 'r')
print(f2.read())
