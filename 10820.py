# coding: utf-8

import sys

big = [chr(i) for i in range(65, 91)]
small = [chr(i) for i in range(97, 123)]
numbers = [str(i) for i in range(10)]


results = []

while True:
    try:
        result = [0 for _ in range(4)]
        line = input()
        for c in line:
            if c in small:
                result[0] += 1
            elif c in big:
                result[1] += 1
            elif c in numbers:
                result[2] += 1
            else:
                result[3] += 1
        results.append(result)
    except EOFError:
        break

for result in results:
    result = list(map(str, result))
    print(" ".join(result))

