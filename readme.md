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
2. 1. approve of the first string number "two", and dismiss "one" as "ne" => didn't work
2. 2. trying to change the overlapping string with an edge case dictionary can work with two overlapping digits given its simplicity => didn't work because of the occurence of three or more overlapping digits.
3. solved by adding the first and last character of the keys into the string.

