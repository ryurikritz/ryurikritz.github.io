# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:04:01 2020

@author: ritam
"""

age = 30  #integer

print(age)
PI = 3.14159 #float
print(PI)
RADIANS_TO_DEGREES = 180/PI
print(RADIANS_TO_DEGREES)
maths_operation = 1 + 3 * 4 / 2 -2
print(maths_operation)

float_division = 12 / 3
print(float_division)
integer_division = 12 // 3  #This does not round the numbers but removes everything after decimals
print(integer_division)
division_with_remainder = 13 // 5
print(division_with_remainder)
remainder = 13 % 5
print(remainder)
x = 37
remainder = x % 2
print(remainder)

my_string = "Hello, World!!"
my_newstring = 'Hello, World'
print(my_string)
string_with_quotes = "Hello, it's me."
another = 'He said " You are amazing" yesterday'
another_format = "He said \"You were amazing!\" yesterday." #Escaping (putting a backslash in front of a character) is used in Python to remove meaning from a character. In this example, we remove Python's meaning of "starting or ending a string"
 # multi line string coming up
multiline = """Hello, world.
 My name is Ryurik. Welcome to my Program.
 """
print(multiline)
"""
Strings
Multiline strings can also be used as ways of commenting sections instead of hashes
It just creates a string and it is not used or called anywhere
"""
name = "Ryurik"
greeting = "Hello, " + name
print(greeting)

age = 34
age_str = str(age)
print("You are " + age_str)
#Usage of the f string in Python in later versions of Python
name = "Ryu"
greeting = f"How are you, {name}?"
print(greeting)
name = "Ritz"
print(greeting)

#Passing variables and values inside strings
name = "Ryurik"
final_greeting = "How are you, {}?"
ryu_greeting = final_greeting.format(name)
print(ryu_greeting)
ritz_greeting = ryu_greeting.format("Ritz")
print(ritz_greeting)
#Final iteration of strings usage of Formats Function
name = "Ryu"
final_greeting = "How are you, {name}?"
ryu_greeting = final_greeting.format(name="Ryu")
print(ryu_greeting)
# Introduction of the Input Function which always gives you a string as default input
my_name = "Ritz"
your_name = input("Enter your name: ")
print(f"Hello {your_name}. My name is {my_name}.")
age = input("Enter your age: ")
age_num = int(age)
print(f"You have lived for {age_num * 12} months.")
#Alternately we can use a single line
age = int(input("Enter your age: "))
print(f"You have lived for {age * 12} months.")
#nice way to label is important
age = int(input("Enter your age: "))
months = age * 12
print(f"You have lived for {months} mnths.")
# Learning Booleans
age = 20
is_overage = age >= 18
is_underage = age < 18
is_twenty = age == 20
# Simple Program
my_number = 5
user_number = int(input("Enter a number: "))
matches = my_number == user_number
print(f"You got it right: {matches}")
# Boolean Continued
age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150
print(f"You can learn programming: {can_learn_programming}.")
# Retirement program code
age = int(input("Enter your age: "))
usually_not_working = age < 18 or age > 65
print(f"At {age}, you are usually not working: {usually_not_working}.")
#Alternate retirement program
age = int(input("Enter your age: "))
usually_working = age >= 18 and age <=65
print(f"At {age}, you are usually working: {usually_working}.")

# Bool values
# and gives you the first value if it is False, otherwise it gives you the second value
x = 35 and 0
print(x)
# OR gives you the first value if it is True, otherwise it gives ou the second value
x = 35 or 0
print(x)
# 0 is false
#used cases are depicted below
name = ""
surname = "Smith"
greeting = name or f"Mr. {surname}"
print(greeting)
#User interaction present
name = input("Enter your name: ")
surname = input("Enter your surname: ")
greeting = name or f"Mr. {surname})"
print(greeting)
#Not value - Not false is True and Not True is False
print(not True)
print(not bool(35))
# Creating lists which should be related and homogeneous. Numbers, strings or other lists
friends = ["Rolf", "Bob", "Anne"]
print(friends[0])
print(len(friends))
friends1 = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
print(friends1[0][0]) # Print Bobs name
print(friends1[1][1]) # Print Bobs age
friends2 = [
        ["Rolf", 24],
        ["Bob", 30],
        ["Anne", 27],
        ["Jen", 25],
]
# to add to list we use the append function. A List is a data structure
friends3 = ["Rolf", "Bob", "Anne"]
friends3.append("Jen")
print(friends3)
# to remove from a list we use the remove function
friends = ["Rolf", "Bob", "Anne"]
friends.remove("Bob")
print(friends)
# For removing a full list which is an element of a larger list, all individual elements should be mentioned
friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
friends.remove(["Anne", 27])
print(friends)
# Tuple is used to define like a list but it has a difference
short_tuple = "Rolf", "Bob"
a_bit_clearer = ("Rolf", "Bob")
#Tuple within a list
tuple_in_ist = [("Rolf", "Bob")]
# To add an element the append function cannot be used with a tuple
# Direct addition to existing elements in tuple is not possible except by the following method
friends = ("Rolf", "Bob", "Anne"
friends = friends + ("Jen",))
print(friends)
# The tuple did not change but we used the same variable. In Tuples we cannot add elements
# SETS Do not contain duplicate elements and DO NOT Keep order even while appending elements
art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}
art_friends.add("Jen")  # add function adds elements to a SET
print(art_friends)
art_friends.remove("Jen")  # remove function removes elements from a SET
print(art_friends)
# Usefulness of SETS
art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}
art_but_not_science = art_friends.difference(science_friends) 
science_but_not_art = science_friends.difference(art_friends)
print(art_but_not_science)
print(science_but_not_art)
# Elements NOT in both sets are called Symmetric difference
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)
# Elements in both sets are called with help of Intersection Function
art_and_science = art_friends.intersectiob(science_friends)
print(art_and_science)
# All friends without any duplicates is called by Union Function
all_friends = art_friends.union(science_friends)
print(all_friends)
# DICTIONARY is used to store Keys and Values. No Duplicates. It maintains the orders in which keys were added to them
friend_ages = {"Rolf":24, "Adam": 30, "Anne": 27}
print(friend_ages["Rolf"])
# Assigning a key in a value of the Dictionary which does not exist yet
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25
print(friend_ages)
# Program which stores information about your friends. For multiple friends if multiple pieces of information is present
# USE A LIST OR A TUPLE OF DICTIONARIES
#Below we are using a tuple inside the Dictionary
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30}
    {"name": "Anne Pun", "age": 27}
)
#Below we are accessing the first element in Tuple in the dictionary and the name property in the tuple
print(friends[0]["name"])
print(friends[2]["name"])
# Use of DICt which is used to turn Data into a Dictionary
friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend_ages = dict(friends)
print(friend_ages)
# Sum and Length Function
grades = [80, 75, 90, 100]
total = sum(grades)
length = len(grades)
average = total /length
print(average)
# Used case for Grades calculation program- List gives you all power , Tuple in future need to modify so may be a bad choice, Dict is worst as repetion is not allowed
# Join allows you to print lists a bit better
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")


