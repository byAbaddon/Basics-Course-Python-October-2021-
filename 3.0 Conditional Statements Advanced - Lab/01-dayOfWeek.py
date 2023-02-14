import calendar

try: print(calendar.day_name[int(input()) - 1])
except: print('Error')

# --------------------------------------------(2)----------------------
lst = ["Error", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
try:
    print(lst[int(input())])
except:
    print('Error')

#------------------------------------------(3)--------------------------------
def fun(arg):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher.get(arg, "Error")


print(fun(int(input())))


# 7
# output: Sunday
    
# ----------------------------------------(4)--------------------------- Warning not work in Judge in this time

match int(input()) :
    case 1: r = 'Monday'
    case 2: r = 'Tuesday'
    case 3: r = 'Wednesday'
    case 4: r = 'Thursday'
    case 5: r = 'Friday'
    case 6: r = 'Saturday'
    case 7: r = 'Sunday'
    case other: r ='Error'
print(r)

    
