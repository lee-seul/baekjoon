# coding: utf-8

def find_bit(num):
    result = []
    num = list(bin(num)[2:])
    num.reverse()
    for i in range(len(num)):
        if int(num[i]):
            result.append(i)
    
    for bit in result:
        print(bit, end=" ")
    

t = int(input())

for _ in range(t):
    find_bit(int(input()))

