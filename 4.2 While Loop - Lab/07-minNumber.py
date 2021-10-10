print(min([int(x) for x in iter(input, 'Stop')]))

'''
100
99
80
70
Stop

output: 70
'''
# -------------------------------------second solution
# min_num = 100000000
#
# while True:
#     try:
#         current = int(input())
#         if min_num > current:
#             min_num = current
#     except:
#         print(min_num)
#         break
