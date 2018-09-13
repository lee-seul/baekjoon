# coding: utf-8


dice = {'1': 'Yakk', '2': 'Doh', '3': 'Seh', '4': 'Ghar', '5': 'Bang', '6': 'Sheesh'}
twice = {'1-1': 'Habb Yakk', '2-2': 'Dobara', '3-3': 'Dousa', '4-4': 'Dorgy',
         '5-5': 'Dabash', '6-6': 'Dosh', '6-5': 'Sheesh Beesh'}


t = int(input())

for i in range(t):
    nums = sorted(input().split(), reverse=True)
    string = '-'.join(nums)
    if string in twice:
        result = twice[string]
    else:
        a, b = nums
        result = '{} {}'.format(dice[a], dice[b])
    print('Case {}: {}'.format(i+1, result))
