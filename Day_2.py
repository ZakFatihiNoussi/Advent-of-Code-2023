
with open("Day_2_input.txt", 'r') as Day_2_input:

    lines = [line.strip('\n') for line in Day_2_input.readlines()]
    game_dict = {}
    selected_keys = []
    

    for line in lines:
        key, values_str = line.split(":")
        game_number = key.split()[1]
        game_dict[game_number] = values_str.strip()
    
    for key, values in game_dict.items():
        red_max = 12
        green_max = 13
        blue_max = 14

        game_scenarios = values.split(';')

        valid = all(
            int(quantity) <= limit
            for scenario in game_scenarios
            for color_quantity in scenario.split(',')
            if (quantity := color_quantity.strip().split()[0]).isdigit()
            for color, limit in zip(['red', 'green', 'blue'], [red_max, green_max, blue_max])
            if color in color_quantity
        )

        if valid:
            selected_keys.append(key)
print(selected_keys)
x = 0
sum = 0
for i in selected_keys:
    sum += int(selected_keys[x])
    x += 1
print(sum)


    
        

        


