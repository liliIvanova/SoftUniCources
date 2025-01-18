FACEBOOK_FEE = 150
INSTAGRAM_FEE = 100
REDDIT_FEE = 50

tabs_cnt = int(input())
salary = int(input())
tab = ''

for n in range(tabs_cnt):
    tab = input()

    if tab == 'Facebook':
        salary -= FACEBOOK_FEE

    elif tab == 'Instagram':
        salary -= INSTAGRAM_FEE

    elif tab == 'Reddit':
        salary -= REDDIT_FEE

    if salary <= 0:
        print('You have lost your salary.')
        break
else:
    print(f'{salary}')