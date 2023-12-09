

with open("Day_1_input.txt", 'r') as Day_1_input :
    lines = [line.strip('\n') for line in Day_1_input.readlines()]

    single_digits_count = 0
    multiple_digits_count = 0
    sum_concatenated_digits = 0
    number_mapping = { 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'nine': 9,'one': 1, 'eight': 8}
    
    for line in lines:

        for word, value in (number_mapping.items()):
            if word in line:
                print(line,word)
                line = line.replace(word, str(value))
        
        
    
        digit_count = sum(char.isdigit() for char in line)

        if digit_count == 1:
            single_digits_count += 1
        elif digit_count > 1:
            multiple_digits_count += 1

        digit_indices = [i for i, char in enumerate(line) if char.isdigit()]


        if len(digit_indices) > 1:
            
            first_digit_index = digit_indices[0]
            last_digit_index = digit_indices[-1]
            result = line[first_digit_index] + line[last_digit_index]
            sum_concatenated_digits += int(result)
            print(result, sum_concatenated_digits)
            

        elif len(digit_indices) == 1:
            digit_index = digit_indices[0]
            digit = line[digit_index]
            result = digit * 2
            sum_concatenated_digits += int(result)
            print(result, sum_concatenated_digits)
        


            
print(f'Sum of concatenated digits: {sum_concatenated_digits}')


print(f'Lines with one single digit: {single_digits_count}')
print(f'Lines with more than one single digit: {multiple_digits_count}')
    

