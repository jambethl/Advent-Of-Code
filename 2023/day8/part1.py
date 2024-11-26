f = open('input.txt')

line_list = []
for line in f.readlines():
    line_list.append(line.strip())

left_right_instructions = line_list[0]

directions_map = {}

for line_index in range(2, len(line_list), 1):
    line_entry = line_list[line_index]
    direction = line_entry[0:line_entry.find(' ')].strip()
    left_direction = line_entry[line_entry.find('(') + 1 : line_entry.find(',')].strip()
    right_direction = line_entry[line_entry.find(', ') + 1 : line_entry.rfind(')')].strip()

    directions_map[direction] = [left_direction, right_direction]

required_steps = 0
current_step = 0
curr_key = None
while True:
    if current_step >= len(left_right_instructions):
        current_step = 0

    if curr_key == None:
        curr_key = 'AAA'

    if curr_key != 'ZZZ':
        required_steps += 1
    else:
        break

    if left_right_instructions[current_step] == 'L':
        next_key = directions_map[curr_key][0]
    else:
        next_key = directions_map[curr_key][1]

    curr_key = next_key
    current_step += 1

print(required_steps)




