budget, video, cpu, ram = [float(input()) for _ in range(4)]
discount = video > cpu
video *= 250
cpu *= video * 0.35
ram *= video * 0.10
total_sum = video + cpu + ram

if discount:
    total_sum *= 0.85

print(f'You have {budget - total_sum:.2f} leva left!' if total_sum <= budget
      else f'Not enough money! You need {total_sum - budget:.2f} leva more!')


'''
900
2
1
3

output: You have 198.75 leva left!
'''