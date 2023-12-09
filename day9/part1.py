f = open('input2.txt')

histories = []
def populate_histories():
    for line in f.readlines():
        history = []
        for num in line.strip().split():
            history.append(int(num))
        histories.append(history)


def get_next_num_for_history(history_list):
    sub_history = []

    for i in range(len(history_list) - 1):
        sub_history.append(history_list[i + 1] - history_list[i])

    if not any(sub_history):
        return sub_history[-1] + history_list[-1]

    next_num = get_next_num_for_history(sub_history)

    return history_list[-1] + next_num

def solve():
    populate_histories()

    total_sum = 0
    for history in histories:
        total_sum += get_next_num_for_history(history)
    return total_sum

answer = solve()
print(answer)
