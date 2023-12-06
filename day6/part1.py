
time_distance_map = {
        41: 249,
        77: 1362,
        70: 1127,
        96: 1011
        }

win_count = [0, 0, 0, 0]

race_num = 0
for time, distance in time_distance_map.items():

    max_distance = distance

    for i in range(time):
        curr_distance = i * (time - i)
        if curr_distance > max_distance:
            win_count[race_num] += 1

    race_num += 1

answer = 1
for num in win_count:
    answer *= num

print(answer)
