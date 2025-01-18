first_code = int(input())
second_code = int(input())

for code in range(first_code, second_code + 1):
    if code == second_code:
        print(chr(code))
    else:
        print(chr(code), end=' ')