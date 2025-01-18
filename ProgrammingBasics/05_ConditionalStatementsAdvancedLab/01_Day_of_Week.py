# Напишете програма, която чете цяло число, въведено от потребителя,
# и отпечатва ден от седмицата (на английски език), в граници [1...7] или отпечатва "Error" в случай, че въведеното число е невалидно.

number = int(input())

if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("Error")


# number = int(input())
#
# day_of_week = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     7: "Sunday"
# }
#
# if 1 <= number < 8:
#     print(day_of_week[number])
# else:
#     print("Error")