# coding: utf-8

x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

result_x, result_y = 0, 0

if x.count(x[0]) == 2:
    result_x = x[2]
else:
    result_x = x[0]

if y.count(y[0]) == 2:
    result_y = y[2]
else:
    result_y = y[0]

print(result_x, result_y)

