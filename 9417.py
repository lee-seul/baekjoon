# coding: utf-8 


def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)


def get_max_gcd(numbers):
    result = 0
    for i, number in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            value = gcd(number, numbers[j])
            if value > result:
                result = value
    return result


n = int(input())

for _ in range(n):
    numbers = list(map(int, input().split()))
    print(get_max_gcd(numbers))
