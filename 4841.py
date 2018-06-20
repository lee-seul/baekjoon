# coding: utf-8 


def solution(number):
    result = ''
    count = 1
    n = number[0]
    for i, num in enumerate(number):
        if i == 0:
            continue

        if n == num:
            count += 1
        
        else:
            result += str(count) + str(n)
            count = 1
            n = num
    result += str(count) + str(n)
    return result


n = int(input())

for _ in range(n):
    number = input()
    print(solution(number))
