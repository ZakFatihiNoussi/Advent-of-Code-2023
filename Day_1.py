

with open("Day_1_input.txt", 'r') as Day_1_input :
    lines = [line.strip('\n') for line in Day_1_input.readlines()]

    sum_concatenated_digits = 0
    number_mapping = {'two': 2, 'one': 1 , 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


    for line in lines:
        
        for word, value in (number_mapping.items()):
            print(line)
            if word in line:
                first_char = word[0]
                last_char = word[-1]
                line = line.replace(word, f"{first_char}{value}{last_char}")

        digit_indices = [i for i, char in enumerate(line) if char.isdigit()]


        if len(digit_indices) > 1:
            
            first_digit_index = digit_indices[0]
            last_digit_index = digit_indices[-1]
            result = line[first_digit_index] + line[last_digit_index]
            sum_concatenated_digits += int(result)

        elif len(digit_indices) == 1:
            digit_index = digit_indices[0]
            digit = line[digit_index]
            result = digit * 2
            sum_concatenated_digits += int(result)
         
print(f'Sum of concatenated digits: {sum_concatenated_digits}')
    

