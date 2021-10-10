sum_num = int(input())
increase_num = 0

while True:
    increase_num += int(input())
    if sum_num <= increase_num:
        print(increase_num)
        break


'''
100
10
20
30
40

output: 100
'''
