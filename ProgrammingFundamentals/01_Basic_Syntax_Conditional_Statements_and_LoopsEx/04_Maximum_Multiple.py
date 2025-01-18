divisor = int(input())
boundary = int(input())

# largest_divisible = 0
#
# for i in range(1, boundary + 1):
#     div = i % divisor
#
#     if div == 0 and largest_divisible < i:
#         largest_divisible = i
#
# print(largest_divisible)

for i in range(boundary, divisor - 1, -1):
    if i % divisor == 0:
        break

print(i)