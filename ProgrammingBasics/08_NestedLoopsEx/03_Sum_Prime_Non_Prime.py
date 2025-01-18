prime_sum = 0
non_prime_sum = 0
num = 0

while True:
    n = input()

    if n == 'stop':
        break

    num = int(n)

    if num < 0:
        print('Number is negative.')
        continue
    else:
        isPrime = True

        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            prime_sum += num
        else:
            non_prime_sum += num

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')