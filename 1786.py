# coding: utf-8


def get_pattern(p):
    """part부분에서 접두사와 접미사가 동일한 최대 길이를 계산
    """
    n, j = len(p), 0
    pattern = [0 for i in range(n)]
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = pattern[j - 1]
        if p[i] == p[j]:
            j += 1
            pattern[i] = j
    return pattern


def find_substring(string, part):
    """KMP 알고리즘 활용
    """
    result = []
    pattern = get_pattern(p)
    n, m, j = len(string), len(part), 0
    for i in range(n):
        while j > 0 and string[i] != part[j]:
            j = pattern[j - 1]
        if string[i] == part[j]:
            if j == m - 1:
                result.append(i - m + 1)
                j = pattern[j]
            else:
                j += 1
    return result


s, p = input(), input()
result = find_substring(s, p)

print(len(result))
for index in result:
    print(index+1, end=" ")
