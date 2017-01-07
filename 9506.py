# coding: utf-8

def is_perfect(n):
    result = []
    for i in range(1, n//2+1):
        if n % i == 0:
            result.append(i)
    if sum(result) == n:
        return result
    return False

while True:
    n = int(input())
    if n == -1:
        break
    l = is_perfect(n)
    if l:
        print(n, "=", " + ".join(map(str,l)))
    else:
        print("{} is NOT perfect.".format(n))


