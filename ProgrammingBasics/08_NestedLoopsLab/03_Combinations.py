n = int(input())
combinations_ctr = 0

for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if x1 + x2 + x3 == n:
                combinations_ctr += 1

print(combinations_ctr)
