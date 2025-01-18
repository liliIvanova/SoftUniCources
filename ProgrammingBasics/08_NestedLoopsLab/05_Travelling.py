saved_money = 0

destination = input()

while destination != 'End':
    money_needed = float(input())

    while saved_money < money_needed:
        saving = float(input())
        saved_money += saving
    else:
        print(f'Going to {destination}!')
        saved_money = 0
        destination = input()