

with open("Day_1_input.txt", 'r') as Day_1_input :
    lines = [line.strip() for line in Day_1_input.readlines()]

    for line in lines:
        if any(char.isdigit() for char in line):
            print("moving on")
        else:
            print(f'The lin "{line}" does not contain a digit.')
    

