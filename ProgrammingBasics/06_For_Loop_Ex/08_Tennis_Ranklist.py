W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720

gained_points = 0
wins_cnt = 0

tournament_cnt = int(input())
points = int(input())

for _ in range(tournament_cnt):
    final_stage = input()

    if final_stage == 'W':
        gained_points += W_POINTS
        wins_cnt += 1

    elif final_stage == 'F':
        gained_points += F_POINTS

    elif final_stage == 'SF':
        gained_points += SF_POINTS

points = points + gained_points

average_points = gained_points // tournament_cnt
won_tournaments_perc = wins_cnt / tournament_cnt * 100

print(f"Final points: {points}")
print(f"Average points: {average_points:.0f}")
print(f"{won_tournaments_perc:.2f}%")
