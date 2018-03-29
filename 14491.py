# coding: utf-8

from math import log

t = int(input())


max_digit = int(log(t, 9))

digits = list(range(max_digit + 1))
digits.reverse()

result = ''
for digit in digits:
    divide = 9 ** digit
    if t >= divide:
        mod = t // divide
        t -= divide * mod
        
        result += str(mod)
    else:
        result += '0'

print(result)

