import re

with open("Day_2_input.txt", 'r') as Day_2_input:
    lines = [line.strip('\n') for line in Day_2_input.readlines()]
    game_dict = {}
    selected_keys = []
    color_limits = {
            "red": 12,
            "green": 13,
            "blue": 14
        }

    for line in lines:
        key, values_str = line.split(":")
        game_number = key.split()[1]
        game_dict[game_number] = values_str.strip()
    
        

        


