# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
# •	Пилешко меню –  10.35 лв.
# •	Меню с риба – 12.40 лв.
# •	Вегетарианско меню  – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.
# Вход
# От конзолата се четат 3 реда:
# •	Брой пилешки менюта – цяло число в интервала [0 … 99]
# •	Брой менюта с риба – цяло число в интервала [0 … 99]
# •	Брой вегетариански менюта – цяло число в интервала [0 … 99]
# Изход
# Да се отпечата на конзолата един ред:  "{цена на поръчката}"

CHICKEN = 10.35
FISH = 12.40
VEGGIE = 8.15
DESSERT_PERC = 20/100
DELIVERY = 2.50

chicken_cnt = int(input())
fish_cnt = int(input())
veggie_cnt = int(input())

sum_no_dessert = CHICKEN * chicken_cnt + FISH * fish_cnt + VEGGIE * veggie_cnt
sum_with_dessert = sum_no_dessert + sum_no_dessert * DESSERT_PERC
sum = sum_with_dessert + DELIVERY

print(sum)