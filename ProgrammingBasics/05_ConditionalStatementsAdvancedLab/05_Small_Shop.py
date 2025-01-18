# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	            0.50	0.80	1.20	1.45	1.60
# Plovdiv	        0.40	0.70	1.15	1.30	1.50
# Varna	            0.45	0.70	1.10	1.35	1.55
# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число),
# въведени от потребителя, и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град.

product = input()
town = input()
amount = float(input())

price = 0

if town == "Sofia":
    if product == "coffee":
        price = amount * 0.50
    elif product == "water":
        price = amount * 0.80
    elif product == "beer":
        price = amount * 1.20
    elif product == "sweets":
        price = amount * 1.45
    elif product == "peanuts":
        price = amount * 1.60
elif town == "Plovdiv":
    if product == "coffee":
        price = amount * 0.40
    elif product == "water":
        price = amount * 0.70
    elif product == "beer":
        price = amount * 1.15
    elif product == "sweets":
        price = amount * 1.30
    elif product == "peanuts":
        price = amount * 1.50
elif town == "Varna":
    if product == "coffee":
        price = amount * 0.45
    elif product == "water":
        price = amount * 0.70
    elif product == "beer":
        price = amount * 1.10
    elif product == "sweets":
        price = amount * 1.35
    elif product == "peanuts":
        price = amount * 1.55

print(price)