# coding: utf-8

while True:
    name, age, weight = input().split()
    if name == '#' and age == '0' and weight == '0':
        break
    result = 'Junior'
    if int(age) > 17 or int(weight) >= 80:
        result = 'Senior'

    print('{} {}'.format(name, result))
