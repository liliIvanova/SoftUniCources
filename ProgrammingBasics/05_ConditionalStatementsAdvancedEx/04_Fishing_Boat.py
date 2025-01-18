# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова, че решават да отидат на риболов с кораб.
# Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# •	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  -  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка,
# която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# Вход
# От конзолата се четат три реда:
# •	Бюджет на групата - цяло число;
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари - цяло число.
# Изход
# На конзолата да се отпечата следното:
# •	Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

SPRING_RENT = 3000
SUMMER_AUTUMN_RENT = 4200
WINTER_RENT = 2600

GROUP_OF_6_DISCOUNT = 10/100
GROUP_OF_7_11_DISCOUNT = 15/100
GROUP_OF_12_DISCOUNT = 25/100

EVEN_NUM_DISCOUNT = 5/100

budget = int(input())
season = input()
fisherman_cnt = int(input())

price = 0
err = True

if season == "Spring":
    err = False
    price = SPRING_RENT

elif season == "Summer" or season == "Autumn":
    err = False
    price = SUMMER_AUTUMN_RENT

elif season == "Winter":
    err = False
    price = WINTER_RENT

if fisherman_cnt <= 6:
    price -= price * GROUP_OF_6_DISCOUNT
elif 7 <= fisherman_cnt <= 11:
    price -= price * GROUP_OF_7_11_DISCOUNT
else:
    price -= price * GROUP_OF_12_DISCOUNT


if not fisherman_cnt % 2 and season != "Autumn":
    price -= price * EVEN_NUM_DISCOUNT

if not err:
    if budget >= price:
        print(f"Yes! You have {(budget - price):.2f} leva left.")
    else:
        print(f"Not enough money! You need {(price - budget):.2f} leva.")