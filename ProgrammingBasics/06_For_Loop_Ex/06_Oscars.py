POINTS_LIMIT = 1250.5

actor_name = input()
academy_points = float(input())
judges_cnt = int(input())
result = ''

for _ in range(1, judges_cnt + 1):
    judge_name = input()
    judge_points = float(input())

    academy_points += (len(judge_name) * judge_points) / 2

    if academy_points >= POINTS_LIMIT:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {abs(POINTS_LIMIT - academy_points):.1f} more!")
