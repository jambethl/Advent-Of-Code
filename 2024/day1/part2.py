f = open('input2.txt')

left_list = []
right_list = []
for line in f:

    left_num = line[0: line.find(" ")]
    right_num = line[line.find(" ") : len(line)]

    left_list.append(int(left_num))
    right_list.append(int(right_num))

answer = 0
already_encountered = []
for i in range(len(left_list)):
    if left_list[i] in already_encountered:
        continue
    i_count = 0
    for j in range(len(right_list)):
        if (right_list[j] == left_list[i]):
            i_count += 1

    answer += left_list[i] * i_count

print(answer)

