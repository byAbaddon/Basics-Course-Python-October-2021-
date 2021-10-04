from math import floor

record, trace, meters_min = [float(input()) for x in range(3)]
swimming_trace = trace * meters_min
add_seconds = floor(trace / 15) * 12.5
time = swimming_trace + add_seconds

if time >= record:
    time = time - record
    print(f'No, he failed! He was {time:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')

# 10464, 1500, 20
