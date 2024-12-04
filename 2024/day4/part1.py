f = open('input.txt')

line_list = []
for line in f:
    line_list.append(list(line.strip()))

rows = len(line_list)
columns = len(line_list[0])

def check_for_xmas_string(row_index_1, row_index_2, row_index_3, column_index_1, column_index_2, column_index_3):
    if row_index_1 < rows and row_index_1 >= 0:
        if row_index_2 < rows and row_index_2 >= 0:
            if row_index_3 < rows and row_index_3 >= 0:
                if column_index_1 < columns and column_index_1 >= 0:
                    if column_index_2 < columns and column_index_2 >= 0:
                        if column_index_3 < columns and column_index_3 >= 0:
                            m = line_list[row_index_1][column_index_1]
                            a = line_list[row_index_2][column_index_2]
                            s = line_list[row_index_3][column_index_3]

                            if m + a + s == 'MAS':
                                return 1
    return 0

xmas_count = 0
for row in range(rows):
    for column in range(columns):
        if line_list[row][column] == 'X':
            xmas_count += check_for_xmas_string(row - 1, row - 2, row - 3, column, column, column)
            xmas_count += check_for_xmas_string(row + 1, row + 2, row + 3, column, column, column)
            xmas_count += check_for_xmas_string(row, row, row, column - 1, column - 2, column - 3)
            xmas_count += check_for_xmas_string(row, row, row, column + 1, column + 2, column + 3)
            xmas_count += check_for_xmas_string(row - 1, row - 2, row - 3, column - 1, column - 2, column - 3)
            xmas_count += check_for_xmas_string(row + 1, row + 2, row + 3, column + 1, column + 2, column + 3)
            xmas_count += check_for_xmas_string(row - 1, row - 2, row - 3, column + 1, column + 2, column + 3)
            xmas_count += check_for_xmas_string(row + 1, row + 2, row + 3, column - 1, column - 2, column - 3)

print(xmas_count)
