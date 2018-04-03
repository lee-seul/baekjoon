# coding: utf-8 


def reverse_num(number):
    number = list(str(number))
    number.reverse()
    result = ''.join(number)
    return int(result)



n, k = map(int, input().split())

m = 0

for i in range(1, k+1):
    temp = n * i
    temp = reverse_num(temp)
    if m < temp:
        m = temp

print(m)

