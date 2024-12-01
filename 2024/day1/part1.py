f = open('input.txt')

left_list = []
right_list = []
for line in f:

    left_num = line[0: line.find(" ")]
    right_num = line[line.find(" ") : len(line)]

    left_list.append(int(left_num))
    right_list.append(int(right_num))

left_list.sort()
right_list.sort()
answer = 0
for num in range(len(left_list)):
    if left_list[num] > right_list[num]:
        answer += left_list[num] - right_list[num]
    else:
        answer += right_list[num] - left_list[num]

    print(answer)
    
