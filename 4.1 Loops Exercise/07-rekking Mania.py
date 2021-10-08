loop = int(input())
groups = [int(input()) for _ in range(loop)]
all_people = sum(groups)


def calc(min_val, max_val):
    current_group = sum(filter(lambda x: min_val <= x <= max_val, groups))
    return f'{current_group / all_people * 100:.2f}%'


print('\n'.join([calc(0, 5), calc(6, 12), calc(13, 25), calc(26, 40), calc(41, 1000)]))

# or
# data = [(0, 5), (6, 12), (13, 25), (26, 40), (41, 1000)]
# for t in data:
#     print(calc(t[0], t[1]))

'''
5
25
41
31
250
6
'''
