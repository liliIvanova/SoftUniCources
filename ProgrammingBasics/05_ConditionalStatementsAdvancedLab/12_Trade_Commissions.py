# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
# Град	0 ≤ s ≤ 500	500 < s ≤ 1 000	1 000 < s ≤ 10 000	s > 10 000
# Sofia	5%	7%	8%	12%
# Varna	4.5%	7.5%	10%	13%
# Plovdiv	5.5%	8%	12%	14.5%
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя, и изчислява и
# извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка. При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".


town = input()
sales = float(input())

commission = 0
err = True

if town == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * 5/100
        err = False
    elif 500 < sales <= 1000:
        commission = sales * 7/100
        err = False
    elif 1000 < sales <= 10000:
        commission = sales * 8/100
        err = False
    elif sales > 10000:
        commission = sales * 12/100
        err = False
    else:
        err = True
elif town == "Varna":
    if 0 <= sales <= 500:
        commission = sales * 4.5/100
        err = False
    elif 500 < sales <= 1000:
        commission = sales * 7.5/100
        err = False
    elif 1000 < sales <= 10000:
        commission = sales * 10/100
        err = False
    elif sales > 10000:
        commission = sales * 13/100
        err = False
    else:
        err = True
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 5.5/100
        err = False
    elif 500 < sales <= 1000:
        commission = sales * 8/100
        err = False
    elif 1000 < sales <= 10000:
        commission = sales * 12/100
        err = False
    elif sales > 10000:
        commission = sales * 14.5/100
        err = False
    else:
        err = True
else:
    err = True

if err:
    print("error")
else:
    print(f"{commission:.2f}")