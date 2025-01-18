budget = int(input())
price = 0

while budget >= 0:
    end = input()

    if end == 'End':
        if budget >= 0:
            print('You bought everything needed.')
            break

    price = int(end)
    budget -= price

else:
    print('You went in overdraft!')