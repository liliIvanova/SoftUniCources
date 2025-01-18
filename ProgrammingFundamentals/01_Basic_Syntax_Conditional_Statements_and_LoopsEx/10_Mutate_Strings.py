first_str = input()
second_str = input()

previous_str = first_str

for ch in range(len(first_str)):
    left_part = second_str[:ch + 1]
    right_part = first_str[ch + 1:]
    new_str = left_part + right_part

    if new_str != previous_str:
        print(new_str)
        previous_str = new_str