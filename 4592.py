# coding: utf-8

def remove_duplicate(num_list):
    tmp = 100
    for i in range(len(num_list)):
        if num_list[i] != tmp:
            yield num_list[i]
        tmp = num_list[i]
    yield "$"

# result = []

while True:
    submit = list(map(int, input().split()))
    if not submit[0]:
        break

    for value in remove_duplicate(submit[1:]):
        print(value, end=" ")
    print()

"""
    tmp = []
    for i in range(1, submit[0]+1):
        if submit[i] not in tmp:
            tmp.append(submit[i])
    result.append(tmp)

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=" ")
    print("$")
    """
