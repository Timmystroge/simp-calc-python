# Developer: TimmyStroge
# Dev GitHub: https://github.com/Timmystroge
# Happy Coding!

from math import* #Import Math

whatDoWeWantToDo = "now lets build a simple Calculator App"
print(whatDoWeWantToDo + "\n")

#? once the user runs the app ask for their name and tell them the app intruction
user = input("Welcome, What is Your Name?: ").upper() # Change the user input to uppercase
print("HELLO " + user + ", WITH THIS SIMPLE CALCULATOR, YOU CAN ONLY CALCULATE 2 NUMBERS AT A TIME")

#? ask for the numbers the user wants to calculate
number1 = float(input("Enter Number 1: ")) #! Number 1
operation = input("Operation e.g plus, minus, divide, multiply: ") #! operation
number2 = float(input("Enter Number 2: ")) #! number2

#? perfom the user calculation
def add(value1, value2): #todo: this function will add the two provided numbers
    calculate = ceil(value1 + value2)
    result = "Dear " + user + ", Your Calcution Result is " + str(calculate)
    print("\n" + result)

def subtract(value1, value2): #todo: this function will subtract the two provided numbers
    calculate = ceil(value1 - value2)
    result = "Dear " + user + ", Your Calcution Result is " + str(calculate)
    print("\n" + result)

def divide(value1, value2): #todo: this function will divide the two provided numbers
    calculate = ceil(value1 / value2)
    result = "Dear " + user + ", Your Calcution Result is " + str(calculate)
    print("\n" + result)

def multiply(value1, value2): #todo: this function will multiply the two provided numbers
    calculate = ceil(value1 * value2)
    result = "Dear " + user + ", Your Calcution Result is " + str(calculate)
    print("\n" + result)

#? PROCESS THE CALCULATION BASED ON THE USER'S OPERATION
if operation == "plus": #todo: IF USER OPERATES TO ADD
    add(number1, number2)
elif operation == "minus": #todo: IF USER OPERATES TO SUBTRACT
    subtract(number1, number2)
elif operation == "divide": #todo: IF USER OPERATES TO DIVIDE
    divide(number1, number2)
elif operation == "multiply": #todo: IF USER OPERATES TO MULTIPLY
    multiply(number1, number2)
else:  print("\n Oops, something went Wrong, Seems you didn't follow the intruction! Try Again Bitch.")

#? Lol
print("\n Thanks for using our App!")

#Python Sweet sha!😂😂😂
#No Need To Trace Curly Brackets { } Up and Down😭😭😂💃