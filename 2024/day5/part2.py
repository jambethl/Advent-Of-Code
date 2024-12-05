f = open('input2.txt')

has_hit_breakpoint = False
numbers_that_must_come_after = {}
cant_come_before = {}
valid_lines = []

for line in f:
    if line == "\n":
        has_hit_breakpoint = True
        continue
    
    if not has_hit_breakpoint:
        left = line[0 : line.find('|') ].strip()
        right = line[line.find('|') + 1::].strip()

        if left in numbers_that_must_come_after:
            numbers_that_must_come_after[left].append(right)
        else:
            numbers_that_must_come_after[left] = [right]

        if right in cant_come_before:
            cant_come_before[right].append(left)
        else:
            cant_come_before[right] = [left]

    else:

        num_line = line.strip().split(',')
        is_valid = True
        for num in range(len(num_line)):

            if num_line[num] in numbers_that_must_come_after:

                for after_num in range(num, len(num_line)):

                    if num_line[after_num] not in numbers_that_must_come_after[num_line[num]]:
                        if num_line[after_num] in numbers_that_must_come_after:
                            if num_line[num] in numbers_that_must_come_after[num_line[after_num]]:
                                temp = num_line[num]
                                num_line[num] = num_line[after_num]
                                num_line[after_num] = temp
                                is_valid = False
                                after_num = 0
            else:
                for after_num in range(num, len(num_line)):
                    if num_line[num] in cant_come_before:
                        if num_line[after_num] in cant_come_before[num_line[num]]:
                            temp = num_line[after_num]
                            num_line[after_num] = num_line[num]
                            num_line[num] = temp
                            is_valid = False
                            after_num = 0
        if not is_valid:
            valid_lines.append(num_line)

answer = 0
for valid_line in valid_lines:
    answer += int(valid_line[len(valid_line)//2])

print(answer)




