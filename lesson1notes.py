'''
*** LESSON 1 NOTES ***
'''

# When you see code that is commented out in this file - feel free to uncomment it and run the file (python lesson1notes.py)
# to see what happens, feel free to play around with it! I'll use block comments for commenting useful code rather than lesson notes
# so you can just remove the ''' from above/below sections of code.
# feel free to uncomment code examples starting with the # but they're mostly used for examples.

# ******* VARIABLES AND TYPES *******

# Variables are data that you may or may not know the value of. They are stored in memory.
# Think of them as a box containing a value, which has a name you can use to reference the value!

'''
i_am_a_variable = "I am a value!" #this is a variable of type string
print(i_am_a_variable) # print is an inbuilt function in pythons standard library, it takes an argument of what to print to console! We can pass it variables or raw types
'''

# As it says on the tin - they can vary so you can change them dynamically.
# A variables type refers to its "data type" the most basic of which are:
# Boolean (True or False)
# Integer (Whole numbers)
# String (text)
# Float (floating point number - e.g. decimal)
# Python is dynamically typed which means you don't have to state or know the types of your variables and they can change.

# Feel free to uncomment the following comment block (remove the ' marks from above and below the block) to play with the code

'''
firstname = "sean" #strings
is_cool = False #bool (boolean)
age = 12  #int
centimeter_height = 200.56 #float
firstname = 100 # this doesn't make sense (names aren't numbers) but it's not an error - it'll run fine.

print(age)
print(is_cool)
print(firstname)
'''

# ******* Quick number primer *******

# In Python, you can perform various mathematical operations on numbers, including integers and floats.
# Some common operations include addition (+), subtraction (-), multiplication (*), and division (/).
# You've used some of these already!

# When performing division, you can get a float result even if you divide two integers.
# For example, 5 / 2 would result in 2.5.

# You can use the "//" operator to perform floor division, which always rounds down to the nearest integer.
# For example, 5 // 2 would result in 2, not 2.5.

# When you need to round to the nearest integer, you can use the "round()" function
# Note that if a float is half way between e.g. 1.5 - round(1.5) is generous and will result in 2!

# our_number = 1
# our_number = our_number + 1 # Our number is now two!

# The above can also be written as:

'''
our_number = 1
our_number += 5 #  Our number is now 6!
our_number -= 1 #  Our number is now 5!
print(our_number)
'''


# ******* Boolean logic *******

# Boolean logic refers to running code based on whether something is True or False
# We've already seen the Boolean type instantiated like this
# i_am_a_boolean = True

# The most basic way we can interact with booleans is in if/else code blocks - this is called control flow.
# The code that is indented (use tab) under the if statement will run if the condition is true
# else the code under the else block will run

'''
if True:
    print("this always prints true")
else:
    print("this will never be reached")
'''

# The above commented code is to show how if/else works - based on some condition (in this example always true)
# Then you can conditionally run some code, if it isn't true you can run the else code.

# That code is kind of useless because the condition is always true. But we can assess variables that may be true of false
# and we can also use operators which compare data

# There are lots of "comparison operators" we can use in python that evaluate to boolean!
# Here are some comparison operators 

# == tests for "is equal to"
# != tests for "not equal to"
# >  tests for " is greater than"
# < tests for "is less than"
# >= tests for "greater than or equal to"
# <= tests for "less than or equal to"

'''
i_am_a_one = 1
i_am_a_two = 2

if i_am_a_one + i_am_a_two == 3:
    print("1 plus two equals 3!")
else:
    print("Something redefined our one and two variables, woops!")
'''

# There are lots of "comparison operators" we can use in python that evaluate to boolean too!
# Here are some comparison operators 

# == tests for "is equal to"
# != tests for "not equal to"
# >  tests for " is greater than"
# < tests for "is less than"
# >= tests for "greater than or equal to"
# <= tests for "less than or equal to"

# 1 > 2 == True
# 1 < 2 == False
# 1 == 2 == False
# 1 != 2 == True
# 1 <= 1 == True
# 2 >= 3 == False

# It's important to note that some of these operators can work on more than integers
# e.g. the '==' operator can test two strings

'''
name = "sean"
coolest_programmer = "sean"
if name == coolest_programmer:
    print(f"{name} is the coolest programmer")
'''

# this print(f"{variable_name}") syntax is a new way of using print, if we want to print the value of variables we can use this syntax to include the variables
# rather than having to concatenate the variables with the string using + 
# as you may have guessed, this will print out "sean is the coolest programmer"

# ******* if/elif/else *******

# We can make if slightly more advanced by adding the concept of "else ifs"
# imagine a scenario where you want to do something if one thing is true, or another if another thing is true, or some default thing if neither is true
# we can add an "elif" block before the else - which operates in exactly the same way as if, but only when the if was false. Check this program out!

'''
user_answer = input("Name one of the two best programmers in the world ")
if user_answer == "sean":
    print("You named the best programmer in the world!")
elif user_answer == "aine":
    print("You named the second best programmer in the world!")
else:
    print("you are flat out wrong mate")
'''
# Try uncommenting this block and typing in "sean", "aine" and any other name. What do you expect to happens? What happens? Feel free to play around.

# ***** Lists *****

# Currently we've been working with primarily variables
# another type of object that is useful is Lists.
# where variables can only contain a single value lists can contain multiple values.
# alist is defined by placing a comma-separated sequence of items inside square brackets [].

# fruits = ["Apples", "Oranges", "Pears"] #This is our list of fruits!

# You can even have a list of mixed data types:
# mixed_list = [42, "apple", 3.14, True]

# To access an item in a list, use its index with the syntax list[index]. Python uses 0-based indexing.
# This means the first item is at index 0, the second at index 1, and so on.
# print(f"The first item in 'fruits' list is {fruits[0]}")

# List objects have several functions that can be performed on them using the dot syntax. To add an item you can:
# fruits.append("Strawberries") # our list is now ["Apples", "Oranges", "Pears", "Strawberries"]


# ******* For Loops *******

# For loops allow us to repeat a block of code a specific number of times or iterate
# through collections like lists.

# A for loop has a specific structure in Python. It typically consists of three main parts:
# 1. The loop variable: This variable changes with each iteration and controls the loop.
# 2. The iterable: The collection or sequence of items you want to loop through, like a list.
# 3. The loop body: The code block to be executed during each iteration.

# Let's start with a basic for loop to print numbers from 1 to 5.

'''
for number in [1, 2, 3, 4, 5]:
    print(number)
'''

# The loop variabole here is number and every iteration represents the next element in the iterable. e.g. 1 then 2 then 3 ...
# The iterable in this case is our list of 1 through 5
# The loop body here is the indented code underneath our definition of the loop - it simply prints the current iterations number

# It's important to note that lists aren't the only iterable in Python, to prove this we can introduce one we've already seen
# Strings are also iterable!

'''
for character in "hello":
    print(char)
'''

# This prints every character in "hello" on a newline! (Newlines at the end of the value are inherent to print)
# h
# e
# l
# l
# o

# ******* Functions and Scope *******

# We've already used some functions such as print. Tou can define your own functions which do things that you define.
# Functions start with the def keyword - then the name of your function followed by its arguments in brackets 
# (if there are any arguments you need to accept otherwise you simply open and close brackets)

# The other important part of a function is that it may or may not contain the return keyword
# all the return keyword does is send back some data to whatever called the function.

# let's create a program which defines a function that takes a list of fruits and counts how many we have that demonstrates these principles

'''
def count_fruits(fruit_basket):
    index = 0 # we need to initialize this before the loop so we can add to it without it being redefined every time the loop starts
    for _ in fruit_basket: #the underscore here means we don't care about the variable for a singular fruit because we don't care about it
        # if we defined index = 0 here as its starting point, we would constantly be setting it to 0 when the loop starts to the next iteration
        index += 1
    return index #return the value of our index variable back to whatever called this function. In this instance it's a print function so the value will be printed

fruits = ['Apple', 'Orange']
fruits.append('Strawberry')
print(count_fruits(fruits)) # this will print how many fruits we have! Three.
'''

# Note that we don't have to match the variable names that we send/receive with functions (but can if we want). The first argument we send is the first argument received
# then the function uses a "copy" of that variables for its own use with its own name that is only available within that function

# Lets write a slightly more complicated function which proves it's usefulnes - reducing code duplication.

# You are organising a party! Some friends have already said yes but you need to write a program to add a friend ad hoc
# Except there is one friend... "Satan" which you don't want to arrive but you know you'll accidentally run this program and invite when you're drunk
# We're going to include safeguards in the program to ensure you CANNOT invite satan.

'''
def print_friends(friends): #local scope variable
    for friend in friends: 
        if friend != "satan": # remember != means not equal to
            print(friend)

friends = ["sean", "laura"]
print("Currently coming to the party are: ")
print_friends(friends)
friends.append(input("Which other friend is coming? "))
print("Cool! The new list is:")
print_friends(friends) 

# the function has saved us typing out several lines of code twice, we just need to call the function a second time.
# This also means if we ever want to change the code, we can just change the function body.

'''
# Try adding satan when the program asks you to, what do you expect to happen? What happens?

# *** Hope you learned something! Here ends lesson 1 ***