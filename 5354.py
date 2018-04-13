# coding: utf-8


n = int(input())

start = '#'
in_box = 'J'
for x in range(n):
    j = int(input())
    
    if j == 1:
        print(start)
    else:
        for i in range(j):
            if i == 0 or i == j -1:
                print(start * j)
            else:
                print('#' + (in_box * (j-2)) + '#')

    if x != n-1:
        print()

