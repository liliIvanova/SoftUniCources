number_of_letters = int(input())
ascii_sum = 0

for _ in range(number_of_letters):
    letter =  input()
    ascii_sum += ord(letter)

print(f'The sum equals: {ascii_sum}')
