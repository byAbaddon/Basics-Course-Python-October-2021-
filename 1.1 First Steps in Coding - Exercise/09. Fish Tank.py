long, width, height, percent = [float(input()) for _ in range(4)]
size = long * width * height * 0.001
percent = percent * 0.01
print(size * (1 - percent))

'''
85
75
47
17

output: 248.68875
'''