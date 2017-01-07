# coding: utf-8

def is_onedigit(num):
    return len(str(num)) == 1

def make_onedigit(num):
    while not is_onedigit(num): 
        num = str(num)
        num = sum(list(map(int, num)))
    return num

while True:
    n = int(input())
    if n == 0:
        break
    print(make_onedigit(n))

