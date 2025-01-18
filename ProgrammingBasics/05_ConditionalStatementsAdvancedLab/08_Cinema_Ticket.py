# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя и
# принтира на конзолата цената на билет за кино според деня от седмицата:

day_of_week = input()

price = 0

if day_of_week == "Wednesday" or day_of_week == "Thursday":
    price = 14
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    price = 16
else:
    price = 12

print(price)