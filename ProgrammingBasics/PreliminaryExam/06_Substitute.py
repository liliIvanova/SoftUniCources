A_FIXED_LIMIT = 8
B_FIXED_LIMIT = 9
C_FIXED_LIMIT = 8
D_FIXED_LIMIT = 9
VALID_CHANGES_LIMIT = 6

k = int(input())
l = int(input())
m = int(input())
n = int(input())

ab = 0
cd = 0
valid_changes_cnt = 0
end_flag = False

a_inc_step = 0
b_inc_step = 0
c_inc_step = 0
d_inc_step = 0

a_lower_limit = 0
a_upper_limit = 0
b_lower_limit = 0
b_upper_limit = 0
c_lower_limit = 0
c_upper_limit = 0
d_lower_limit = 0
d_upper_limit = 0


if k <= A_FIXED_LIMIT:
    a_inc_step = 1
    a_lower_limit = k
    a_upper_limit = A_FIXED_LIMIT + 1
else:
    a_inc_step = -1
    a_lower_limit = k
    a_upper_limit = A_FIXED_LIMIT - 1

if l >= B_FIXED_LIMIT:
    b_inc_step = 1
    b_lower_limit = B_FIXED_LIMIT
    b_upper_limit = l + 1
else:
    b_inc_step = -1
    b_lower_limit = B_FIXED_LIMIT
    b_upper_limit = l - 1

if m <= C_FIXED_LIMIT:
    c_inc_step = 1
    c_lower_limit = m
    c_upper_limit = C_FIXED_LIMIT +  1
else:
    c_inc_step = -1
    c_lower_limit = m
    c_upper_limit = C_FIXED_LIMIT - 1

if n >= D_FIXED_LIMIT:
    d_inc_step = 1
    d_lower_limit = D_FIXED_LIMIT
    d_upper_limit = n + 1
else:
    d_inc_step = -1
    d_lower_limit = D_FIXED_LIMIT
    d_upper_limit = n - 1

for a in range(a_lower_limit,a_upper_limit, a_inc_step):

    if a % 2 != 0:
        continue

    for b in range(b_lower_limit, b_upper_limit, b_inc_step):

        if b % 2 == 0:
            continue

        ab = a * 10 + b

        for c in range(c_lower_limit, c_upper_limit, c_inc_step):

            if c % 2 != 0:
                continue

            for d in range(d_lower_limit, d_upper_limit, d_inc_step):

                if d % 2 == 0:
                    continue

                cd = c * 10 + d

                if valid_changes_cnt < VALID_CHANGES_LIMIT:

                    if ab != cd:
                        print(f'{a}{b} - {c}{d}')
                        valid_changes_cnt += 1
                    else:
                        print('Cannot change the same player.')

                else:
                    end_flag = True
                    break

            if end_flag:
                break

        if end_flag:
            break

    if end_flag:
        break
