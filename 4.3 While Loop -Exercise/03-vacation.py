holiday_price = float(input())
budget = float(input())
spend, days = 0, 0

while budget < holiday_price:
    action = input()
    amount = float(input())
    days += 1
    if action == "save":
        budget += amount
        spend = 0
    elif action == "spend":
        if amount >= budget:
            budget = 0
        else:
            budget -= amount
        spend += 1
        if spend == 5:
            break

if budget >= holiday_price:
    print(f"You saved the money for {days} days.")
else:
    print(f"You can't save the money.\n{days}")
    

