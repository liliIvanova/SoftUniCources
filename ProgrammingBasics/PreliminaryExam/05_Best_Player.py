HET_TRICK_GOALS = 3
GOALS_LIMIT= 10

best_player = ' '
max_goals_num = 0
result = ' '

while True:
    player_name = input()

    if player_name == 'END':
        break

    goals = int(input())

    if goals > max_goals_num:
        max_goals_num = goals
        best_player = player_name

    if goals >= HET_TRICK_GOALS:
        result = f'He has scored {max_goals_num} goals and made a hat-trick !!!'
    else:
        result = f'He has scored {max_goals_num} goals.'

    if goals >= GOALS_LIMIT:
        break

print(f'{best_player} is the best player!')
print(result)