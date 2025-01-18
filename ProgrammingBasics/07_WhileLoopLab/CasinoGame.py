import random

import emoji

USER_ID = 1445
user_lost_counter = 0
user_profit_counter = 0
print(emoji.emojize("grape"))

fruits = ['\U0001F600', '\U0001F44D', ':apple', 'watermelon']

balance = int(input('Enter your initial balance:'))

while balance > 0:
    print(f'Your current balance is: {balance:.2f} euro!')

    bet = int(input('Place your bet: '))

    while bet > balance:
        print('Insufficient balance. Please a bet within your balance.')
        bet = int(input('Place your bet'))

    if USER_ID == 1445 and user_lost_counter > 10000 and bet < 500:
        print(f'Congratulations! You won the jackpot - {bet * 10:.2f} euro!')
        print(fruits[2], fruits[2], fruits[2])
        balance += bet*10
        user_lost_counter = 0
        continue

    reel1 = random.choice(fruits)
    reel2 = random.choice(fruits)
    reel3 = random.choice(fruits)

    print(reel1, reel2, reel3)

    if reel1 == reel2 == reel3:
        print(f'Congratulations! You won the jackpot - {bet * 10:.2f} euro!')
        balance += bet * 10

    elif reel1 == reel2:
        print(f'Congratulations! You won  - {bet * 2:.2f} euro!')
        balance += bet * 2

    else:
        print('Sorry, you lost! Try again!')
        balance -= bet

if balance <= 0:
    print('Game over! Your final balance is:', balance)