
f = open('input.txt')

total_sum = 0
for line in f:
    first = 0
    last = 0
    for char in line:
        if char.isnumeric():
            first = char
            break
    for char in line[::-1]:
        if char.isnumeric():
            last = char
            break

    line_sum = int(first + last)

    total_sum += int(first + last)

print(total_sum)

