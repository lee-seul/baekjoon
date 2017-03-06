# coding: utf-8

numbers = list(map(int, input().split()))
order = input()
l = ["A", "B", "C"]
numbers.sort()

dic = {}

for i in range(3):
    dic[l[i]] = numbers[i] 

for o in order:
    print(dic[o], end=" ")

