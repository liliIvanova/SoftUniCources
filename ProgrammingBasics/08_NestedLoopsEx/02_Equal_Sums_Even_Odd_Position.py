n1 = int(input())
n2 = int(input())

for i in range(n1, n2 + 1):
    even_sum = 0
    odd_sum = 0
    number_str = str(i)

    for idx, digit in enumerate(number_str):
        if idx % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(i, end=' ')
