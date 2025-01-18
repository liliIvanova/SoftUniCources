number = input()

largest = number
length = len(number)

for i in range(length):
    for j in range(1,length -1):
        if number[i] < number[j]:
            largest[i] = number[j]

print(largest)