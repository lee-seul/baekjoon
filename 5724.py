# coding: utf-8

def solution(num):
    result = 0
    for i in range(1, num+1):
        result += i**2
    return result

while True:
    n = int(input())
    if not n:
        break
    print(solution(n)) 
