STEPS_GOAL = 10000

total_steps = 0

while True:
    command = input()

    if command == 'Going home':
        steps_to_home = int(input())
        total_steps += steps_to_home
        if total_steps < STEPS_GOAL:
            print(f'{STEPS_GOAL - total_steps} more steps to reach goal.')
            break
    else:
        steps = int(command)
        total_steps += steps

    if total_steps >= STEPS_GOAL:
        print(f'Goal reached! Good job!\n{total_steps - STEPS_GOAL} steps over the goal!')
        break