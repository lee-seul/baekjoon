# coding: utf-8

from math import log

m, n = list(map(int, input().split()))

if m != 0:
    max_digit = int(log(m, n))
    digits = list(range(max_digit + 1))

    digits.reverse()

    numbers = {n:chr(55+n) for n in range(10, 16)}

    result = ''
    for digit in digits:
        divide = n ** digit
        if m >= divide:
            mod = m // divide
            m -= divide * mod 
            if mod >= 10:
                result += numbers[mod]
            else:
                result += str(mod)

        else:
            result += '0'

        if m == 0:
            if digit >= 0:
                temp = '0' * digit
                result += temp
            break
else:
    result = '0'

print(result)

