import re

f = open('input.txt')

result = 0
for line in f:

    my_nums = [entry.strip() for entry in re.sub(' +', ' ', line[line.find("|") + 2 : len(line) - 1]).split(" ")]
    winning_nums = [entry.strip() for entry in re.sub(' +', ' ', line[line.find(":") +2  : line.find("|")-1]).split(" ")]

    line_result = 0
    for winning in winning_nums:
        if winning in my_nums and winning.isnumeric():
            if line_result == 0:
                line_result = 1
            else:
                line_result *= 2

    result += line_result

    print(result)
