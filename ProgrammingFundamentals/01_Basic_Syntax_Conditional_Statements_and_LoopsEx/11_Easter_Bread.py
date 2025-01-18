# budget = float(input())
# flower_per_kg_price = float(input())
#
# eggs_price = flower_per_kg_price * 75 /100
# milk_price = flower_per_kg_price * 25/100 + flower_per_kg_price
#
# eggs_num = 0
# loafs_num = 0
# price_with_milk = flower_per_kg_price + eggs_price + milk_price
# price_no_milk = flower_per_kg_price + eggs_price
#
# money_spent = 0
#
# # recire:
# # eggs 1 pack
# # flower 1kg
# # milk 0.250 l
#
#
# while True:
#
#     if loafs_num % 4 == 0:
#         bread_price = price_with_milk
#     else:
#         bread_price = price_no_milk
#
#     if budget - money_spent >= bread_price:
#         money_spent += bread_price
#         loafs_num += 1
#         eggs_num += 3
#
#         if loafs_num % 3 == 0:
#             eggs_num -= (loafs_num - 2)
#
#     else: # not enough budget -> end
#         print(f'You made {loafs_num} loaves of Easter bread! Now you have {eggs_num} eggs and {budget - money_spent:.2f}BGN left.')
#         break


budget = float(input())
flower_per_kg_price = float(input())

eggs_price = flower_per_kg_price * 75 /100
milk_price = (flower_per_kg_price * 25/100 + flower_per_kg_price) / 4

eggs_num = 0
loafs_num = 0
bread_price = flower_per_kg_price + eggs_price + milk_price

# recire:
# eggs 1 pack
# flower 1kg
# milk 0.250 l


while True:

    if budget >= bread_price:
        budget -= bread_price
        loafs_num += 1
        eggs_num += 3

        if loafs_num % 3 == 0:
            eggs_num -= (loafs_num - 2)

    else: # not enough budget -> end
        print(f'You made {loafs_num} loaves of Easter bread! Now you have {eggs_num} eggs and {budget:.2f}BGN left.')
        break
