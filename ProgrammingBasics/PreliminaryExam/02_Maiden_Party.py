LOVE_LETTER_PRICE = 0.6
WAX_ROSE_PRICE = 7.2
KEYHOLDER_PRICE = 3.6
CARICATURE_PRICE = 18.20
LUCKY_SURPRISE_PRICE = 22.00

DISCOUNT_LIMIT = 25
DOSCOUNT = 35/100

HOSTING_EXPENCES = 10/100

party_price = float(input())
love_letters_cnt = int(input())
wax_roses_cnt = int(input())
keyholders_cnt = int(input())
caricatures_cnt = int(input())
lucky_surprises_cnt = int(input())

total_sales_income = (love_letters_cnt * LOVE_LETTER_PRICE +
                      wax_roses_cnt * WAX_ROSE_PRICE +
                      keyholders_cnt * KEYHOLDER_PRICE +
                      caricatures_cnt * CARICATURE_PRICE +
                      lucky_surprises_cnt * LUCKY_SURPRISE_PRICE)

total_ordered_cnt = love_letters_cnt + wax_roses_cnt + keyholders_cnt + caricatures_cnt + lucky_surprises_cnt

if total_ordered_cnt > DISCOUNT_LIMIT:
    total_sales_income -= total_sales_income * DOSCOUNT

total_sales_income -= HOSTING_EXPENCES * total_sales_income


if total_sales_income >= party_price:
    print(f'Yes! {total_sales_income - party_price :.2f} lv left.')
else:
    print(f'Not enough money! {party_price - total_sales_income:.2f} lv needed.')

