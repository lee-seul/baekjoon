# coding: utf-8

def biggest_prime(num):
    if num < 2:
        return 1
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return num - (num / i)
    return num - 1

n = int(input())

print(int(biggest_prime(n)))
