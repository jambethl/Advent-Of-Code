f = open('input.txt')

valid_nums = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"]

def get_digit(line, index):
    if line[index].isnumeric():
        return line[index]
    return None

def get_first_word(line, index):
    for num_word in valid_nums:
        if index + len(num_word) <= len(line):
            word = line[index:index + len(num_word)]
            if (word in valid_nums):
                return str(valid_nums.index(word) + 1) # use the index as the word -> int
    return None

def get_last_word(line, index):
    for num_word in valid_nums:
        if index - len(num_word) - 1 >= 0:
            word = line[index-len(num_word) - 1:index - 1]
            if (word in valid_nums):
                return str(valid_nums.index(word) + 1)
    return None

def calculate_first_last_sum():
    total_sum = 0
    for line in f:
        first = 0
        last = 0
        for char in range(len(line)):
            first = get_digit(line, char)
            if (first == None):
                first = get_first_word(line, char)
            if (first):
                break

        for char in range(len(line), 0, -1):
            last = get_digit(line, char - 1)
            if (last == None):
                last = get_last_word(line, char)
            if (last):
                break

        total_sum += int(first + last)

    print(total_sum)

calculate_first_last_sum()

