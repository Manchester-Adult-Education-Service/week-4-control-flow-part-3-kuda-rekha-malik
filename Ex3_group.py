# -------------------------------------------
# Exercise 3: Group Exercise
# -------------------------------------------
# Work in groups of 2–3 students.
# Create one shared Python program together using:
# - Variables
# - Input & Output
# - Decision Making (if / elif / else)
# Use GitHub Classroom to share your work and practice collaboration.

# Workflow:
# 1. Each learner uses their own computer in turn.
# 2. Pull latest changes: git pull origin main
# 3. Add code / fix errors / test program
# 4. git add, commit, push
# 5. Next learner repeats steps 2–4

# -------------------------------------------
# Task 1: Personal Information
# -------------------------------------------
# Note: Read all of the instructions below first before starting!

# Ask the user for their name and one other fact, such as:
# - favourite colour
# - favourite hobby
# Store these in variables and print a message using f-strings.

# Example of syntax only (not the answer):
# print(f"{person_name} enjoys painting")  # Use your own variables and fact

# TODO:
# 1. Ask for your name using input()
# 2. Ask for one personal fact (food, colour, or hobby)
# 3. Print a message using your variables and f-strings

# Write your code below:
name1= input("What is your name: ")
favourite_food= input("What is your favourite food: ")
print(f"Hello, {name1} likes {favourite_food}")
# Now switch to the next learner's computer!

# -------------------------------------------
# Task 2: Simple Decision
# -------------------------------------------
# Note: Read all of the instructions below first before starting!

# Ask the user for their age (integer).
# Compare their age to a number (like 18 or 21).
# Use one if-else statement.
# Print one message if the condition is True, another message if False.

# Example of syntax only:
# if some_condition:
#     print("You may attend the club")  # Example message, not your answer
# else:
#     print("You must wait")            # Example message, not your answer

# TODO:
# 1. Ask for the user's age and convert it to an integer
# 2. Compare it to a number using >, <, ==, or !=
# 3. Print a message if the condition is True and a different message if False

# Write your code below:
age = int(input("What is your age?"))
if age > 18:
    print("You can drive cars")
elif age < 18:
    print("You cannot drive cars")

# Now switch to the next learner's computer!

# -------------------------------------------
# Task 3: Multiple Conditions
# -------------------------------------------
# Note: Read all of the instructions below first before starting!

# Ask the user for their age and a family member's age (integers).
# Compare the two ages using >, <, or ==.
# Use if-elif-else to handle three possible cases:
# - Your age is bigger
# - Both ages are equal
# - Your age is smaller

# Example of syntax only:
# if age1 > age2:
#     print("First person is taller")      # Example message, not your answer
# elif age1 == age2:
#     print("They are the same height")   # Example message, not your answer
# else:
#     print("Second person is taller")    # Example message, not your answer

# TODO:
# 1. Ask for two ages (yours and a family member's)
# 2. Compare the two ages using >, <, ==
# 3. Write if-elif-else statements with three different messages

# Write your code below:
house = int (input ("At what age did you purchase your first house? "))
house2 = int (input ("At what age did your dad purchase his first house? "))
if house > house2:
    print("You've done well. ")
elif house != house2:
    print("Amazing, what an achievement! ")
else:
    print("Great")

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run the following commands:
#    git add Ex3_group.py
#    git commit -m "Completed group exercise"
#    git push origin main
# -------------------------------------------

# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Extension 1:
# Ask for two ages and combine conditions using AND / OR.
# Example scenario: "Is the first age greater than 10 AND the second age less than 20?"
# Use print() to show True or False

# Extension 2:
# Mini quiz: ask the user two questions (numbers or text)
# Use if-elif-else to print different messages depending on the answers
# Example scenario: "If user chooses option1 print 'Option 1 selected', elif option2 print 'Option 2 selected', else print 'Other option'"

# Extension 3 (more challenging):
# Ask for multiple inputs (name, age, favourite colour, food)
# Use nested if statements or logical operators (and/or)
# Example scenario: "If age > 15 AND favourite colour is blue, print 'You like blue and are older than 15', else print another message"
# Write your extension code below:
#STILL WORKING ON THIS:
age_1= int(input("please enter the first age: "))
age_2= int(input("please enter the second age: "))
result_using_and= (age_1>10) and (age_2<20)
result_using_or= (age_1>10) or (age_2<20)
print("first age>10 and second age<20:", result_using_and)
print("first age>10 or second age<20:", result_using_or)

answer_1= (input("What is the capital of Trinidad?: ")).lower()
answer_2= int(input("What is 6/3: "))
if answer_1 == "port of spain" and answer_2 == 2:
    print("Both answers are correct!")
elif answer_1 == "port of spain":
    print("First one is correct but check your maths calculation.")
elif answer_2 == 2:
    print("The maths calculation is right but check your geography.")
else:
    print("Both of your answers are incorrect. Please try again!")

name= (input("What is your name?: "))
age= int(input("What is your age?: "))
favourite_colour= (input("What is your favourite colour?: ")).lower()
favourite_food= (input("What is your favourite food?: ")).lower()
if age>18 and favourite_colour == "blue":
    print(f"{name} is an adult and favourite colour is blue")
elif age<=18 and age>=13 and favourite_food == "baked beans":
    print(f"{name} is an tenager that likes bake beans")
elif age<13 and favourite_colour == "green":
    print(f"{name} is an child that likes green things")
else:
    print(f"{name} age {age} favourite food is {favourite_colour} {favourite_food} can't be classified")

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open terminal
# 3. git add Ex3_group.py
# 4. git commit -m "Completed extension activities"
# 5. git push origin main
# Check GitHub to see your changes.
# -------------------------------------------
