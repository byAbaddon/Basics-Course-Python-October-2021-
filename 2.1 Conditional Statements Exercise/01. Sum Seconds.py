from datetime import datetime, timedelta

result = sum([int(input()) for _ in range(0, 3)])
time = datetime(2021, 10, 3)
delta = timedelta(seconds=result)
print(str(delta)[slice(3, 10)])

'''
35
45
44

output: 2:04
'''