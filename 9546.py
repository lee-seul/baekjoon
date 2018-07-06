# coding: utf-8 


n = int(input())

results = [1]

for i in range(29):
    temp = results[i] + 0.5
    temp *= 2
    results.append(int(temp))


for _ in range(n):
    k = int(input())
    print(results[k-1])
