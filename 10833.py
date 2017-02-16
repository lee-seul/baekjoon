# coding: utf-8

def share_apple(student, apple):
    if student > apple:
        return apple
    n = 2
    while student * n <= apple:
        n += 1
    n -= 1
    result = apple - (student * n)
    return result

n = int(input())

result = 0
for _ in range(n):
    students, apples = map(int, input().split())
    result += share_apple(students, apples)

print(result)

