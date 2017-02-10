# coding: utf-8

k = int(input())

fibo = [0, 1]

for i in range(k-1):
    fibo.append(fibo[i] + fibo[i+1])

print(fibo[-2], fibo[-1])

