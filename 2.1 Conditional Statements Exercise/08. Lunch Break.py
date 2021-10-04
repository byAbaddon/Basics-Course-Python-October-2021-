from math import ceil

move, duration, time_out = [input() if x < 1 else int(input()) for x in range(3)]

lunch = time_out * 100 / 8 / 100
relax = time_out * 100 / 4 / 100
total_time = time_out - lunch - relax

if total_time >= duration:
    print(f'You have enough time to watch {move} and left with {ceil(total_time - duration)} minutes free time.')
else:
    print(f"You don't have enough time to watch {move}, you need {ceil(duration - total_time)} more minutes.")

'''
Game of Thrones
60
96
'''
