# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената за целия престой за студио и апартамент. Цените зависят от месеца на престоя:
#   Май и октомври	            Юни и септември	                Юли и август
# Студио - 50 лв./нощувка	    Студио - 75.20 лв./нощувка	    Студио - 76 лв./нощувка
# Апартамент - 65 лв./нощувка	Апартамент - 68.70 лв./нощувка	Апартамент - 77 лв./нощувка
# Предлагат се и следните отстъпки:
# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.
# Вход
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
# •	На първия ред е месецът - May, June, July, August, September или October;
# •	На втория ред е броят на нощувките - цяло число.
# Изход
# Да се отпечатат на конзолата 2 реда:
# •	На първия ред: "Apartment: {цена за целият престой} lv."
# •	На втория ред: "Studio: {цена за целият престой} lv."
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.

MAY_OCTOBER_STUDIO_PRICE = 50.00
MAY_OCTOBER_APARTMENT_PRICE = 65.00
JUNE_SEPTEMBER_STUDIO_PRICE = 75.20
JUNE_SEPTEMBER_APARTMENT_PRICE = 68.70
JULY_AUGUST_STUDIO_PRICE = 76.00
JULY_AUGUST_APARTMENT_PRICE = 77.00

MAY_OCTOBER_STUDIO_DISCOUNT_7 = 5/100
MAY_OCTOBER_STUDIO_DISCOUNT_14 = 30/100
JUNE_SEPTEMBER_STUDIO_DICOUNT_14 = 20/100

APARTMENT_DISCOUNT_14 = 10/100

month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = nights * MAY_OCTOBER_STUDIO_PRICE
    apartment_price = nights * MAY_OCTOBER_APARTMENT_PRICE

    if 7 < nights <= 14:
        studio_price -= studio_price * MAY_OCTOBER_STUDIO_DISCOUNT_7
    elif nights > 14:
        studio_price -= studio_price * MAY_OCTOBER_STUDIO_DISCOUNT_14

elif month == "June" or month == "September":
    studio_price = nights * JUNE_SEPTEMBER_STUDIO_PRICE
    apartment_price = nights * JUNE_SEPTEMBER_APARTMENT_PRICE

    if nights > 14:
        studio_price -= studio_price * JUNE_SEPTEMBER_STUDIO_DICOUNT_14

elif month == "July" or month == "August":
    studio_price = nights * JULY_AUGUST_STUDIO_PRICE
    apartment_price = nights * JULY_AUGUST_APARTMENT_PRICE

if nights > 14:
    apartment_price -= apartment_price * APARTMENT_DISCOUNT_14

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")