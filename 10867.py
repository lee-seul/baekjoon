# coding: utf-8

import sys
write = sys.stdout.write

n = int(input())
numbers = list(map(int, input().split()))
numbers = list(set(numbers))
numbers.sort()

for number in numbers:
    write(str(number) + " " )

