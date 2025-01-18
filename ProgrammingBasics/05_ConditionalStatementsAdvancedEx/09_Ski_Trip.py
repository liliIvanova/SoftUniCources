ROOM_PRICE = 18.00
APARTMENT_PRICE = 25.00
PRESIDENT_AP_PRICE = 35.00

FIRST_DISCOUNT_LIMIT = 10
SECOND_DISCOUNT_LIMIT = 15

AP_10_DISCOUNT = 30/100
AP_10_15_DISCOUNT = 35/100
AP_15_DISCOUNT = 50/100
PRESIDENT_AP_10_DISCOUNT = 10/100
PRESIDENT_AP_10_15_DISCOUNT = 15/100
PRESIDENT_AP_15_DISCOUNT = 20/100

POSITIVE_RATING_PERC = 25/100
NEGATIVE_RATING_PERC = 10/100

vacation_nights = int(input()) -1
room = input()
rating = input()

price = 0

if room == "room for one person":

    price = vacation_nights * ROOM_PRICE

elif room == 'apartment':

    price = vacation_nights * APARTMENT_PRICE

    if 0 < vacation_nights < FIRST_DISCOUNT_LIMIT:
        price -= price * AP_10_DISCOUNT
    elif FIRST_DISCOUNT_LIMIT <= vacation_nights <= SECOND_DISCOUNT_LIMIT:
        price -= price * AP_10_15_DISCOUNT
    else:
        price -= price * AP_15_DISCOUNT

elif room == 'president apartment':

    price = vacation_nights * PRESIDENT_AP_PRICE

    if 0 < vacation_nights < FIRST_DISCOUNT_LIMIT:
        price -= price * PRESIDENT_AP_10_DISCOUNT
    elif FIRST_DISCOUNT_LIMIT <= vacation_nights <= SECOND_DISCOUNT_LIMIT:
        price -= price * PRESIDENT_AP_10_15_DISCOUNT
    else:
        price -= price * PRESIDENT_AP_15_DISCOUNT

if rating == 'positive':
    price += price * POSITIVE_RATING_PERC
elif rating == 'negative':
    price -= price * NEGATIVE_RATING_PERC

print(f"{price:.2f}")
