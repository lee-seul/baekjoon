# coding: utf-8


t = int(input())

for _ in range(t):
    amount, measure = input().split()
    amount = float(amount)
    if measure == 'kg':
        result = 2.2046
        measure = 'lb'
    elif measure == 'lb':
        result = 0.4536
        measure = 'kg'
    elif measure == 'l':
        result = 0.2642
        measure = 'g'
    elif measure == 'g':
        result = 3.7854
        measure = 'l'
    
    print("{:.4f} {}".format(result * amount, measure))

