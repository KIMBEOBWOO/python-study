# while문을 사용해
# 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

n = 3
sum = 3
while n+3 < 1000:
    n += 3
    sum += n
    print(n)  # 더해진 n 의 값이 출력

print(sum)
