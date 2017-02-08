# coding: utf-8

mod = 1000000
p = mod//10*15

fibo = [0, 1]

for i in range(2, p):
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= mod


n = int(input())

print(fibo[n%p])
