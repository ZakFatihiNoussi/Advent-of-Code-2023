import re

with open("Day_3_input.txt", 'r') as Day_3_input:

    engine_schematic = Day_3_input.read()
    engine_schematic = engine_schematic.replace('\n','')
    
    unique_symbols = ['=', '*', '+', '/', '&', '#', '-', '%', '$', '@']
    

    print(len(engine_schematic), engine_schematic[140])







    '''
    pattern = r'[^\w\s\d.]'
    symbols = re.findall(pattern, engine_schematic)
    symbols_string = ''.join(symbols)
    for char in symbols_string:
        if char not in unique_symbols:
            unique_symbols.append(char)
            '''

    







