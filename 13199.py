# coding: utf-8

def count_cp(total, amount, need):
    result = 0
    while total >= need:
        temp = total // need
        result += temp
        total += temp * amount
        total -= temp * need
    return result
    

n = int(input())
for _ in range(n):
    p, m, f, c = map(int, input().split())
    temp = (c * (m//p)) # 현금 결제한 쿠폰 갯수
    result = count_cp(temp, c, f) - temp // f
    print(result)
