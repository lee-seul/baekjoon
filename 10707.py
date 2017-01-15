# coding: utf-8

input_list = []
for _ in range(5):
    input_list.append(int(input()))

x = input_list[0] * input_list[4]
y = input_list[1]
if input_list[2] < input_list[4]:
    y += input_list[3] * (input_list[4] - input_list[2])

if x >= y:
    print(y)
else:
    print(x)
