# Магазин за плодове през работните дни работи на следните цени:
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.50	1.20	0.85	1.45	2.70	5.50	3.85
# През събота и неделя магазинът работи на по-високи цени:
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.70	1.25	0.90	1.60	3.00	5.60	4.20
# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя, и пресмята цената според цените от таблиците по-горе:
# •	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# •	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# •	количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка. При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".

fruit = input()
day_of_week = input()
amount = float(input())

err = True

if day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price = amount * 2.70
        err = False
    elif fruit == "apple":
        price = amount * 1.25
        err = False
    elif fruit == "orange":
        price = amount * 0.90
        err = False
    elif fruit == "grapefruit":
        price = amount * 1.60
        err = False
    elif fruit == "kiwi":
        price = amount * 3.00
        err = False
    elif fruit == "pineapple":
        price = amount * 5.60
        err = False
    elif fruit == "grapes":
        price = amount * 4.20
        err = False
    else:
        err = True
elif day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday"\
        or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        price = amount * 2.50
        err = False
    elif fruit == "apple":
        price = amount * 1.20
        err = False
    elif fruit == "orange":
        price = amount * 0.85
        err = False
    elif fruit == "grapefruit":
        price = amount * 1.45
        err = False
    elif fruit == "kiwi":
        price = amount * 2.70
        err = False
    elif fruit == "pineapple":
        price = amount * 5.50
        err = False
    elif fruit == "grapes":
        price = amount * 3.85
        err = False
    else:
        err = True
else:
    err = True

if err:
    print("error")
else:
    print(f"{price:.2f}")

