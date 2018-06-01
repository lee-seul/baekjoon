# coding: utf-8 


a, b, g = map(int, input().split())


data = []

result_a = 0
result_b = 0

for _ in range(3):
    temp = input().split()
    data.append(temp)


for i in range(g):
    if data[2][i] in data[0]:
        result_a += 1
    else:
        result_b += 1

if result_a > result_b:
    print('A')

if result_a == result_b:
    print('TIE')

if result_b > result_a:
    print('B')



