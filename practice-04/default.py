# def many(name, *args):
#     print('my name is ', name)
#     print(args)
#     print(type(args))


# name = '김법우'

# many(name, 0, 1, 2, 3, 4, 5, 6, 7)


# def many_kw(**kwargs):
#     print(kwargs)


# many_kw(a=1, b=3, c=[1, 2, 3, 4])


# def mul(c, f): return c*f


# print(mul(3, 4))

f = open('./newFile.txt', 'w')
for i in range(1, 21):
    writeData = "%d 번째 줄입니다.\n" % i
    f.write(writeData)
f.close()

f = open('./newFile.txt', 'r')
line = f.readline()
line = f.readline()
print(line)
lines = f.readlines()

print(lines)
