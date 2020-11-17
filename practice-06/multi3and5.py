# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.


# 내 풀이
# 1. 3의 배수를 모두 구한다
# 2. 5의 배수를 모두 구한다
# 3. 3과 5의 공배수를 제거한다 -> or 연산

def threeAndFive():
    n = 1
    origin = []
    while n < 20:
        if(n % 3 == 0 or n % 5 == 0):
            origin.append(n)
        n += 1

    return origin


print(threeAndFive())
