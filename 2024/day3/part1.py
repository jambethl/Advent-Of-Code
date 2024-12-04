import re

f = open('input.txt')

total = 0
for line in f:
    matches = re.findall('mul\(\d+\,\d+\)', line)

    print(matches)

    
    for match in matches:
        separator_index = match.find(',')

        first_num = int(match[4 : separator_index])
        second_num = int(match[separator_index + 1 : len(match) - 1])

        total += first_num * second_num

print(total)


