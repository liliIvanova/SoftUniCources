# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ.
# Напишете програма, която спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече.
# Вашият приятел има различни планове за всеки етап от деня, които изискват и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# •	Градусите - цяло число;
# •	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".

temp = int(input())
time_of_day = input()

Outfit = ""
Shoes = ""
err = True

if time_of_day == "Morning":
    if 10 <= temp  <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
        err = False
    elif 18 < temp <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        err = False
    else:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        err = False
elif time_of_day == "Afternoon":
    if 10 <= temp  <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        err = False
    elif 18 < temp <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        err = False
    else:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
        err = False
elif time_of_day == "Evening":
    if 10 <= temp <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        err = False
    elif 18 < temp <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        err = False
    else:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        err = False



print(f"It's {temp} degrees, get your {Outfit} and {Shoes}.")
