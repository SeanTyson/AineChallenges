# ******* VARIABLES AND TYPES *******

# python is dynamically typed!!

'''
firstname = "sean" #strings
is_cool = False #bool (boolean)


#this is if/else blocks
if is_cool:
    cool_string = " is cool"
else: #this is the false calls
    cool_string = " is not cool"



print(firstname + cool_string)
# ******* number operations *******

age = 28

#sean ages 5 years

age = age + 5

print(age)


# LOOPS

#You are organising a party! Some friends have already said yes but you need to write a program to add friends ad hoc
'''

def print_friends(friends): #local scope variable
    name = "sean"
    for friend in friends: 
        print(friend)


friends = ["sean", "laura"]
print("Currently coming to the party are: ")

print_friends(friends)

friends.append(input("Which of your other friends are coming? "))
print(name)
print_friends(friends)