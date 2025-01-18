age = int(input())
laundry_machine_price = float(input())
toy_price = int(input())

even_birthday_money = 0
toys_cnt = 0
total_sum = 0

for N in range(1, age +1):

    if N % 2 == 0:
        even_birthday_money += 10 * N/2 -1
    else:
        toys_cnt += 1

total_sum = even_birthday_money + toys_cnt * toy_price

if total_sum >= laundry_machine_price:
    print(f'Yes! {total_sum - laundry_machine_price:.2f}')
else:
    print(f"No! {abs(laundry_machine_price - total_sum):.2f}")
