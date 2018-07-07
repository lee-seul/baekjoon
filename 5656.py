# coding: utf-8


cnt = 1
while True:
    s = input()
    if 'E' in s:
        break

    result = 'true' if eval(s) else 'false'
    print('Case {}: {}'.format(cnt, result))
    cnt += 1
