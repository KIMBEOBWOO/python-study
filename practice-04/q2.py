def avg_all_number(*args):
    sum = 0
    for i in args:
        sum += i
    return sum/len(args)


print(avg_all_number(1, 2, 3, 4, 5, 6, 7, 8, 9))
