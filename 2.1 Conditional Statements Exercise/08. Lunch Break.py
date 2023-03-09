from math import ceil

move, duration, time_out = input(), int(input()), int(input())


lunch = time_out / 8
relax = time_out / 4
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
