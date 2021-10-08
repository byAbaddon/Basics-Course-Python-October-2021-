from math import floor

tournaments = int(input())
stat_points = int(input())
all_points = 0
win = 0

points_obj = {'W': 2000, 'F': 1200, 'SF': 720}

for x in range(tournaments):
    concurrent_tournament = input()
    all_points += points_obj[concurrent_tournament]
    if concurrent_tournament == 'W':
        win += 1

print(f'Final points: {all_points + stat_points}')
print(f'Average points: {floor(all_points / tournaments)}')
print(f'{win / tournaments * 100:.2f}%')

'''
7
1200
SF
F
W
F
W
SF
W
'''
