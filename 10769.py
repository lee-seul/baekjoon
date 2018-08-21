# coding: utf-8


s = input()
happy = s.count(':-)')
sad = s.count(':-(')

if not happy and not sad:
    print('none')
else:
    if sad == happy:
        print('unsure')

    if sad > happy:
        print('sad')

    if sad < happy:
        print('happy')
