with open("Day_3_input.txt", 'r') as Day_3_input:

    engine_schematic = Day_3_input.read()
    engine_schematic = engine_schematic.replace('\n','')
    
    unique_symbols = ['=', '*', '+', '/', '&', '#', '-', '%', '$', '@']
    current_number = ''

    stored_numbers = []
    i = 0

    for char in engine_schematic:
        
        if char.isdigit():            
            current_number += char
            i += 1
            if engine_schematic[i-1] in unique_symbols:
                print(engine_schematic[i-1], 'test')
                

        elif current_number:

            stored_numbers.append(int(current_number))
            current_number = ''

    if current_number:
        stored_numbers.append(int(current_number))


            
            


'''
    pattern = r'[^\w\s\d.]'
    symbols = re.findall(pattern, engine_schematic)
    symbols_string = ''.join(symbols)
    for char in symbols_string:
        if char not in unique_symbols:
            unique_symbols.append(char)
            '''

    







