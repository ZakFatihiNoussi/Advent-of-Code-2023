
with open("Day_2_input.txt", 'r') as Day_2_input:

    lines = [line.strip('\n') for line in Day_2_input.readlines()]
    game_dict = {}
    selected_keys = []
    total_power = 0
    

    for line in lines:
        key, values_str = line.split(":")
        game_number = key.split()[1]
        game_dict[game_number] = values_str.strip()
    

    for key, values in game_dict.items():
        


        red_max = 12
        green_max = 13
        blue_max = 14

        red_limit = 12
        blue_limit = 13
        green_limit = 14

        game_scenarios = values.split(';')
        max_red = max([int(quantity.split()[0]) for scenario in game_scenarios for quantity in scenario.split(',') if 'red' in quantity])
        max_green = max([int(quantity.split()[0]) for scenario in game_scenarios for quantity in scenario.split(',') if 'green' in quantity])
        max_blue = max([int(quantity.split()[0]) for scenario in game_scenarios for quantity in scenario.split(',') if 'blue' in quantity])

        power = max_red * max_green * max_blue
        total_power += power
        print(f"Game {key}: {max_red} red, {max_green} green, {max_blue} blue - Power: {power}")



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
print("Total power:", total_power)

    
        

        


