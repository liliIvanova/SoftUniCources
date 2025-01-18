vacation_money = float(input())
available_money = float(input())

days_cnt = 0
spend_days_cnt = 0

while True:
    spend_save_action = input()
    spend_save_money = float(input())

    days_cnt += 1

    if spend_save_action == 'spend':
        spend_days_cnt += 1

        if available_money <= spend_save_money:
            available_money = 0
        else:
            available_money -= spend_save_money

    elif spend_save_action == 'save':
        spend_days_cnt = 0
        available_money += spend_save_money

    if spend_days_cnt == 5:
        print(f'You can\'t save the money.\n{days_cnt}')
        break

    if available_money >= vacation_money:
        print(f'You saved the money for {days_cnt} days.')
        break

