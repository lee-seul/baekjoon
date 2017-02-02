# coding: utf-8

def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a%b)


t = int(input())


for _ in range(t):
    numbers = list(map(int, input().split()))
    result = 0
    for i in range(1, numbers[0] + 1):
        for j in range(i+1, numbers[0] + 1):
            result += gcd(numbers[i], numbers[j])
    print(result)
