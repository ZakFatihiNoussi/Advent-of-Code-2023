

with open("Day_1_input.txt", 'r') as Day_1_input :
    lines = [line.strip('\n') for line in Day_1_input.readlines()]

    single_digits_count = 0
    multiple_digits_count = 0

    for line in lines:
        digit_count = sum(char.isdigit() for char in line)

        if digit_count == 1:
            single_digits_count += 1
        elif digit_count > 1:
            multiple_digits_count += 1

print(f'Lines with one single digit: {single_digits_count}')
print(f'Lines with more than one single digit: {multiple_digits_count}')
    

