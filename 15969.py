# coding: utf-8


n = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()

print(numbers[-1] - numbers[0])

