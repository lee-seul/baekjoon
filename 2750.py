# coding: utf-8

l = []
n = int(input())
for i in range(n):
    l.append(int(input()))

# 단순 문제 해결
l.sort()

# 삽입 정렬
#a = 0
#for i in range(1, len(l)):
#    val = l[i]
#    for j in range(i-1, -1, -1):
#        if l[j] >= val:
#            l[j+1] = l[j]
#        else:
#            a = j
#            break
#    l[a] = val

# 버블 정렬
#for i in range(len(l)):
#    for j in range(len(l)-1):
#        if l[j] > l[j+1]:
#            tmp = l[j]
#            l[j] = l[j+1]
#            l[j+1] = tmp


for i in l:
    print(i)

