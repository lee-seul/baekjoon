# coding: utf-8


result = []
for i in range(5):
    s = input()
    if 'FBI' in s:
        result.append(str(i+1))

if not result:
    print("HE GOT AWAY!")
else:
    print(' '.join(result))
