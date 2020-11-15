# 다음과 같은 내용을 지닌 파일 test.txt가 있다.
# 이 파일의 내용 중 "java"라는
# 문자열을 "python"으로 바꾸어서 저장해 보자.

init = """
Life is too short
you need java
"""
with open('test.txt', 'w') as f:
    f.write(init)
    print('init text.txt ... \n')

with open('test.txt', 'r') as f:
    data = f.readlines()
    for i in range(len(data)):
        if(data[i].find('java') > 0):
            data[i] = data[i].replace('java', 'python')

    with open('test.txt', 'w') as f2:
        print('re save')
        f2.write("".join(data))
