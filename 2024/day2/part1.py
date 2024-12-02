f = open('input.txt')

valid_reports = 0
for line in f:
    list_of_line_nums = list(map(int, line.split()))

    first = list_of_line_nums[0]
    second = list_of_line_nums[1]

    is_descending = False
    if first > second:
        is_descending = True

    is_valid_line = True
    for i in range(len(list_of_line_nums) - 1):
        current = list_of_line_nums[i]
        next = list_of_line_nums[i + 1]

        if current == next:
            is_valid_line = False
            break

        if is_descending:
            if current < next or current - next > 3:
                is_valid_line = False
                break
        else:
            if next < current or next - current > 3:
                is_valid_line = False
                break

    if is_valid_line:
        valid_reports += 1
print(valid_reports)


