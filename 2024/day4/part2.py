f = open('input.txt')

line_list = []
for line in f:
    line_list.append(list(line.strip()))

rows = len(line_list)
columns = len(line_list[0])

def check_for_xmas_string(row_index_1, row_index_2, column_index_1, column_index_2):
    if row_index_1 < rows and row_index_1 >= 0:
        if row_index_2 < rows and row_index_2 >= 0:
            if column_index_1 < columns and column_index_1 >= 0:
                if column_index_2 < columns and column_index_2 >= 0:
                    # it's 11 pm and i'm too tired to give these variables proper names
                    i = line_list[row_index_1][column_index_1] == 'M' and line_list[row_index_2][column_index_2] == 'S'
                    j = line_list[row_index_1][column_index_1] == 'S' and line_list[row_index_2][column_index_2] == 'M'

                    x = line_list[row_index_1][column_index_2] == 'M' and line_list[row_index_2][column_index_1] == 'S'
                    y = line_list[row_index_1][column_index_2] == 'S' and line_list[row_index_2][column_index_1] == 'M'

                    return (i or j) and (x or y)

    return 0

xmas_count = 0
for row in range(rows):
    for column in range(columns):
        if line_list[row][column] == 'A':
            xmas_count += check_for_xmas_string(row - 1, row + 1, column - 1, column + 1)
print(xmas_count)
