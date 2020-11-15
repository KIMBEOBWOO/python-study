# f = open('test.txt','a')

comment = """
설명
1. 사용자 입력
2. q 입력시 종료 

입력해 주세요 : 
"""
while True:
    with open('test.txt', 'a') as f:
        data = input(comment)
        if(data == 'q'):
            break
        else:
            f.write(data)
            print('\n%s 입력 되었습니다.\n' % data)
