# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day",
# ако е почивен - "Weekend".
# Ако се въведе текст различен от ден от седмицата да се отпечата - "Error".

WORKIG_DAY = 0
WEEKEND = 1
ERROR = 2

day_of_week = input()

day = ERROR

if day_of_week == "Monday":
    day = WORKIG_DAY
elif day_of_week == "Tuesday":
    day = WORKIG_DAY
elif day_of_week == "Wednesday":
    day = WORKIG_DAY
elif day_of_week == "Thursday":
    day = WORKIG_DAY
elif day_of_week == "Friday":
    day = WORKIG_DAY
elif day_of_week == "Saturday":
    day = WEEKEND
elif day_of_week == "Sunday":
    day = WEEKEND
else:
    day = ERROR

if day == WORKIG_DAY:
    print("Working day")
elif day == WEEKEND:
    print("Weekend")
else:
    print("Error")