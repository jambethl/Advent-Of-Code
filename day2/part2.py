f = open('input.txt')

total_sum = 0
for line in f:

    max_color = {
            "red": 0,
            "green": 0,
            "blue": 0
            }

    list_of_games = line[line.find(":") + 2:len(line)-1].split(";")

    for game in list_of_games:

        game_sets = game.strip().split(",")

        for color in game_sets:
            stripped_color = color.strip()

            color_count = stripped_color[0:stripped_color.find(" ")]
            color_name = stripped_color[stripped_color.find(" ") + 1:len(stripped_color)]

            for color_map_entry in max_color:
                if color_map_entry == color_name:
                    if int(color_count) > max_color.get(color_name):
                        max_color[color_name] = int(color_count)

    total_sum += max_color.get("blue") * max_color.get("red") * max_color.get("green")

    print(total_sum)

