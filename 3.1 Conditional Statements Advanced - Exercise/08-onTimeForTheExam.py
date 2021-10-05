# onTimeForTheExam
ex_hour, ex_min, ar_hour, ar_min = [int(input()) for _ in range(4)]

exam_min = ex_min + ex_hour * 60
arrive_min = ar_min + ar_hour * 60

if arrive_min > exam_min:
    print("Late")
elif exam_min - arrive_min <= 30:
    print("On time")
else:
    print("Early")

result = abs(exam_min - arrive_min)
if exam_min - arrive_min > 0:
    if result < 60:
        print(f"{result} minutes before the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours before the start")
elif arrive_min - exam_min > 0:
    if result < 60:
        print(f"{result} minutes after the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours after the start")

# "9","30","9","50"
# "9","00","8","30"
# "16","00","15","00"
# "9","00","10","30"
# "14","00","13","55"
# "11","30","8","12"
# "10","00","10","00"
# "11","30","10","55"
# "11","30","12","29"
