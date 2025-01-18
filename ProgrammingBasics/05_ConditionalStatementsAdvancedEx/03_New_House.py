# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма,
# която да изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен. Различните цветя са с различни цени:
# цвете             	Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	    3.80	2.80	3	    2.50
# Съществуват следните отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

ROSE_PRICE = 5.00
DAHLIA_PRICE = 3.80
TULIP_PRICE = 2.80
NARCISSUS_PRICE = 3.00
GLADIOLUS_PRICE = 2.50

ROSES_DISCOUNT = 10/100
DAHLIAS_DISCOUNT = 15/100
TULIPS_DISCOUNT = 15/100
NARCISSUS_ADD = 15/100
GLADIOLUS_ADD = 20/100

ROSES_THRESHOLD = 80
DAHLIAS_THRESHOLD = 90
TULIPS_THRESHOLD = 80
NARCISSUS_THRESHOLD = 120
GLADIOLUS_THRESHOLD = 80


flowers_type = input()
flowers_cnt = int(input())
budget = int(input())

price = 0
err = True

if flowers_type == "Roses":
    err = False
    price = flowers_cnt * ROSE_PRICE
    if flowers_cnt > ROSES_THRESHOLD:
        price -= price * ROSES_DISCOUNT

elif flowers_type == "Dahlias":
    err = False
    price = flowers_cnt * DAHLIA_PRICE
    if flowers_cnt > DAHLIAS_THRESHOLD:
        price -= price * DAHLIAS_DISCOUNT

elif flowers_type == "Tulips":
    err = False
    price = flowers_cnt * TULIP_PRICE
    if flowers_cnt > TULIPS_THRESHOLD:
        price -= price * TULIPS_DISCOUNT

elif flowers_type == "Narcissus":
    err = False
    price = flowers_cnt * NARCISSUS_PRICE
    if flowers_cnt < NARCISSUS_THRESHOLD:
        price += price * NARCISSUS_ADD

elif flowers_type == "Gladiolus":
    err = False
    price = flowers_cnt * GLADIOLUS_PRICE
    if flowers_cnt < GLADIOLUS_THRESHOLD:
        price += price * GLADIOLUS_ADD

if not err:
    if budget >= price:
        print(f"Hey, you have a great garden with {flowers_cnt} {flowers_type} and {(budget - price):.2f} leva left.")
    else:
        print(f"Not enough money, you need {(price - budget):.2f} leva more.")