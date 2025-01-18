# Петър иска да купи N видеокарти, M процесора и P на брой рам памет.
# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
# Вход
# Входът се състои от четири реда:
# 1.	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2.	Броят видеокарти - цяло число в интервала [1…100]
# 3.	Броят процесори - цяло число в интервала [1…100]
# 4.	Броят рам памет - цяло число в интервала [1…100]
# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# •	Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# •	Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.

VIDEO_CARD_PRICE = 250
CPU_PERC = 35/100
RAM_PERC = 10/100
DISCOUNT = 15/100

budget = float(input())
video_card_cnt = int(input())
cpu_cnt = int(input())
ram_cnt = int(input())

video_cards_price = video_card_cnt * VIDEO_CARD_PRICE
cpu_price = video_cards_price * CPU_PERC * cpu_cnt
ram_price = video_cards_price * RAM_PERC * ram_cnt

total = video_cards_price + cpu_price + ram_price

if video_card_cnt > cpu_cnt:
    total -= total * DISCOUNT

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")

