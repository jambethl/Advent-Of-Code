f = open('input2.txt')

lines = []

for line in f.readlines():
    lines.append(line)

locations = []

string_seeds = lines[0][6:len(lines[0])].strip().split(' ')

seeds = [int(num_string) for num_string in string_seeds]

for seed in seeds:

    print(seed)
    for line in lines:

        if not line[0].isnumeric():
            #if line[0] == '\n':
                #print('\n\nSeed: ' + str(seed) + '\n\n')
            continue

        middle_val = int(line[line.find(' ') + 1 : line.rfind(' ')])

        left_val = int(line[0 : line.find(' ')])
        print("middle " + str(middle_val))

        if seed >= middle_val:

            right_val = int(line[line.rfind(' ') : len(line)])

            print("right " + str(right_val))

            if middle_val + right_val > seed:


                print("left " + str(left_val))

                #remainder = middle_val - left_val



                #seed -= remainder


                remainder = left_val - middle_val

                seed += remainder

                print("seed " + str(seed))
    
        print('\n\nSeed: ' + str(seed) + '\n\n')
    locations.append(seed)


print(locations)

                
