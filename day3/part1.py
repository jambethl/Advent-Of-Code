f = open('input.txt')

symbols = ["*", "#", "+", "$", "@", "%", "/", "&", "_", "-", "="]

def has_symbol_at_x(line, position, num_len):
    if line[position - 1] in symbols:
        return True
    if line[num_len] in symbols:
        return True
    return False

def has_symbol_at_y():
    return False

def has_symbol_diangonal():
    return False

def parse():
    file_as_2d_array = []
    adjacent_num_list = []
    line_num = 0
    for line in f.readlines():

        file_as_2d_array.append(line)

    y = 0
    for line in file_as_2d_array:

        position = 0
        while position < len(file_as_2d_array[0]):

            if line[position].isnumeric():

                window = position
                is_num = True
                while is_num:
                    if line[window] == "." or line[window] in symbols:
                        is_num = False
                    else:
                        if window + 1 < len(file_as_2d_array[0]):
                            window += 1
                        else:
                            is_num = False

                num_substr = line[position:window]

                if has_symbol_at_x(line, position, window):
                    adjacent_num_list.append(num_substr)
                    
                
                if y - 1 != 0:
                    for i in range(position, window, 1):
                        if num_substr == "763":
                            print(file_as_2d_array[y-1][i])
                        if file_as_2d_array[y-1][i] in symbols:
                            adjacent_num_list.append(num_substr)
                if y + 1 < len(file_as_2d_array):
                    for i in range(position, window, 1):
                        if file_as_2d_array[y+1][i] in symbols:
                            adjacent_num_list.append(num_substr)

                if y - 1 != 0 and position - 1 != 0:
                    if file_as_2d_array[y-1][position-1] in symbols:
                        adjacent_num_list.append(num_substr)
                if y - 1 != 0 and window < len(file_as_2d_array[0]):
                    if file_as_2d_array[y-1][window] in symbols:
                        adjacent_num_list.append(num_substr)

                if y + 1 < len(file_as_2d_array) and window  < len(file_as_2d_array[0]):
                    if file_as_2d_array[y+1][window] in symbols:
                        adjacent_num_list.append(num_substr)
                if y + 1 < len(file_as_2d_array) and position - 1 != 0:
                    if file_as_2d_array[y+1][position-1] in symbols:
                        adjacent_num_list.append(num_substr)

                position = window

            else:
                position += 1
        y += 1

        line_num += 1
    desired_array = [int(numeric_string) for numeric_string in adjacent_num_list]
    print(sum(desired_array))


parse()

                    

