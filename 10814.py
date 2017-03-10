# coding: utf-8

n = int(input())
members = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    members.append((age, i, name))

members.sort()

for i in range(n):
    print(members[i][0], members[i][2])
    
