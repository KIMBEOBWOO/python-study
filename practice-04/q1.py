def is_odd(number):
    result = "%d is" % number
    if(number % 2 == 0):
        print(result, "even")
    else:
        print(result, "odd")


is_odd(2)
is_odd(11)
