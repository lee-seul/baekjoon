# coding: utf-8


t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]
    for _ in range(k):
        temp = []
        for i in range(1, n+1):
            temp.append(sum(people[:i]))
        people = temp

    print(people[n-1])
