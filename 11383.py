# coding: utf-8 


def check_double(raw, double, length, width):
    for i in range(length):
        for j in range(width):
            pixel = raw[i][j]
            idx = j*2
            d_pixel = double[i][idx:idx+2]
            d_pixel = ''.join(d_pixel)
            if not  pixel * 2 == d_pixel:
                return False
    return True 


n, m = map(int, input().split())

raw = []
for _ in range(n):
    img = input()
    raw.append(img)

double = []
for _ in range(n):
    img = input()
    double.append(img)


check = check_double(raw, double, n, m)
if check:
    print('Eyfa')
else:
    print('Not Eyfa')

