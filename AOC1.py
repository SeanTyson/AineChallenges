'''
--- Day 1: Not Quite Lisp ---

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?

I want the solve to this puzzle to
A) Take user input which will consist of the '(' and ')' composition 
B) Pass the input to a function you define that figures out which floor santa is on based on the above rules
C) Output which floor santa is on to the terminal

Please review lesson1notes.py which should help you write a program to solve this puzzle. Keep the puzzle in mind while reading :)
'''

floor = 0

directions = input('Give Santa directions pls')

for direction in directions:
    if directions == "(":
        floor = floor +1
    if directions == ")":
        floor = floor -1
print(floor)