# coding: utf-8

n = int(input())
seats = [0 for i in range(101)]

input_list = list(map(int, input().split()))

count = 0
for e in input_list:
    if seats[e]:
        count += 1
    else:
        seats[e] = 1

print(count)
