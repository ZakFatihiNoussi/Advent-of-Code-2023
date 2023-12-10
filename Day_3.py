import re

with open("Day_3_input.txt", 'r') as Day_3_input:

    engine_schematic = Day_3_input.read()
    pattern = r'[^\w\s\d.]'
    symbols = re.findall(pattern, engine_schematic)
    symbols_string = ''.join(symbols)
    print(symbols_string)
    