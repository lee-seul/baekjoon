# coding: utf-8

n = int(input())

for _ in range(n):
    a, b = input().split()
    result = []
    for i in range(len(a)):
        value = ord(b[i]) - ord(a[i])
        value %= 26
        result.append(value)
    
    print("Distances:", end=" ")
    for r in result:
        print(r, end= " ") 
    print()

