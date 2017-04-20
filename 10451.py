# coding: utf-8


def count_cycle(seq, length):
    visited = [0 for _ in range(length)]
    count = 0
    for i in range(length):
        if not visited[i]:
            temp = [i+1]
            cnt = 0
            idx = i
            while cnt < length:
                if seq[idx] in temp:
                    count += 1
                    break
                temp.append(seq[idx])
                idx = seq[idx] - 1
        
            for e in temp:
                visited[e-1] = 1
    return count


t = int(input())

for _ in range(t):
    n = int(input())
    dots = list(map(int, input().split()))
    print(count_cycle(dots, n)) 

