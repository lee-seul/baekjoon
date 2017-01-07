# coding: utf-8

from math import log, ceil

n = int(input())
m = ceil(log(n//3, 2))

def make_triangle(triangle):
    result = [[" " for col in range(len(triangle[0])*2+1)] for row in range(len(triangle)*2)]
    x = (len(result[0])//2 - 1) - (len(triangle[0])//2 -1) 
    y = len(triangle)
    z = len(triangle[0])
    for i in range(y):
        for j in range(z):
            result[i][x+j] = triangle[i][j]
        for k in range(z*2+1):
            if k == z:
                result[y+i][k] == " "
            elif k < z:
                result[y+i][k] = triangle[i][k%z]
            else:
                result[y+i][k] = triangle[i][k%z-1]
    return result

triangle = ["  *  ", " * * ", "*****"]
for i in range(m):
    triangle = make_triangle(triangle)

for i in triangle:
    print("".join(i))


