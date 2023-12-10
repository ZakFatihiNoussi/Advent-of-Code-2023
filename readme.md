### Reminders:
Choose different programming languages to solve the puzzles.

## Puzzle 1:
#### Part 1:
So, we have a text file in which:
1. For each line, we want to extract the first and the last number, in case of one number, we want to replicate it.
2. Concatenate the first and last digit into a two-digit decimal.
3. Then sum up every two digit as the answer.

#### Part 2:
1. before the digit concatenation, we must find string numbers and convert them to their corresponding integer digit.
2. Fix the case in which there are two string numbers attached, for example: twone
- approve of the first string number "two", and dismiss "one" as "ne" => didn't work
- trying to change the overlapping string with an edge case dictionary can work with two overlapping digits given its simplicity => didn't work because of the occurence of three or more overlapping digits.
3. solved by adding the first and last character of the keys into the string.

## Puzzle 2:
#### Part 1:
1. Split each line to an id and its corresponding values
2. Check if there's any number above 12 red cubes, 13 green, 14 blue.
3. sum the id of the ones below or equal the threshold

#### Part 2:
1. find the largest integer for each color for each game and multiply them.
2. sum each game's multiplied integers.

## Day 3:
#### Part 1
1. Extracted all the symbols
2. After omitting all new lines, ended up with a 140 x 140 grid/matrix, so it should start from [0] to [139] then reset.
3. When finding a whole number on a particular line*, check previous/next character if there's a symbol, else if check line before(above) len(found_number[n])+1 and -1, else check the line below in the same way as the line above.


