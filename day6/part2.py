time = 41777096
distance = 249136211271011
ways_to_win = 0

for i in range(time):
    curr_distance = i * (time - i)
    if curr_distance > distance:
        ways_to_win += 1

print(ways_to_win)
