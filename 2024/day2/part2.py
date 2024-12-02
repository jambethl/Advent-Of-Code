
def is_sorted(line):
    return line == sorted(line) or line == sorted(line, reverse = True)

def is_bounds_not_exceeded(line):
    for i in range(1, len(line)):
        if not 1 <= abs(line[i - 1] - line[i]) <= 3:
            return False
    return True


def is_line_safe(line):

    if is_sorted(line) and is_bounds_not_exceeded(line):
        return True

    for i in range(len(line)):
        new = line[:i] + line[i + 1:]
        if is_sorted(new) and is_bounds_not_exceeded(new):
            return True
    return False


def get_answer():
    f = open('input.txt')

    safe_lines = 0
    for line in f:
        list_of_line_nums = list(map(int, line.split()))
        if is_line_safe(list_of_line_nums):
            safe_lines += 1
    return safe_lines

print(get_answer())
