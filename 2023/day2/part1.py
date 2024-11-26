f = open('input.txt')

configuration = {
        "red": 12,
        "green": 13,
        "blue": 14
        }

game_id = 0
total_possible = 0
for line in f:
    game_id += 1

    list_of_games = line[line.find(":") + 2:len(line)-1].split(";")

    is_possible = True
    for game in list_of_games:

        game_sets = game.strip().split(",")

        for color in game_sets:
            stripped_color = color.strip()
            
            color_count = stripped_color[0:stripped_color.find(" ")]
            color_name = stripped_color[stripped_color.find(" ") + 1:len(stripped_color)]

            for config in configuration:
                if config == color_name:
                    if configuration.get(color_name) < int(color_count):
                        is_possible = False
                        break
    if is_possible:
        total_possible += game_id


    print(total_possible)


        
