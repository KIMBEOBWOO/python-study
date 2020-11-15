comment = """
1. Add
2. Del
3. List
4. Quit

Enter Number : """

# n = 0
# while n != 4:
#     print(comment)
#     n = int(input())

test_list = [1, 2, 3, 4, 5, 6, 7]
test_tuple = (1, 2, 3, 4, 5, 6, 7,)

for l in test_list:
    print(l)

print('-'*10)

for t in test_tuple:
    print(t)

print('-'*10)

# 요소 값이 튜플임을 사용한 for문
tuple_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

for (char, number) in tuple_list:
    print(char, ' , ', number)
