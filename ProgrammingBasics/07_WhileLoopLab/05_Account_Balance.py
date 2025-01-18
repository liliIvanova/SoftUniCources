increase = input()
sum = 0

while increase != 'NoMoreMoney':

    current_increase = float(increase)

    if current_increase < 0:
        print('Invalid operation!')
        break
    else:
        sum += current_increase
        print(f'Increase: {current_increase:.2f}')
    increase = input()

print(f'Total: {sum:.2f}')