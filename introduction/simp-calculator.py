# Developer: TimmyStroge
# Dev GitHub: https://github.com/Timmystroge
# Happy Coding!

from math import* #Import Math

whatDoWeWantToDo = "lets build a simple Calculator App"
print(f"{whatDoWeWantToDo} \n")

#? On running the app ask the user for their name and tell them the app's intruction    
# Change the user input to uppercase
user = input("Welcome, What is Your Name?: ").upper() 
print(f"HELLO {user}, WITH THIS SIMPLE CALCULATOR, YOU CAN ONLY CALCULATE 2 NUMBERS AT A TIME")

#? ask for the numbers the user wants to calculate
#!Prompt user to enter Number 1
number1 = float(input("Enter Number 1: ")) 

#!Prompt user to enter math operation
operation = input("Operation e.g plus, minus, divide, multiply: ") 

#!Prompt user to enter Number2
number2 = float(input("Enter Number 2: ")) 

# reuseable function to display result template start
def displayResult(currentUser, calculation):
   result = f"Dear {currentUser}, Your Calculation Result is {str(calculation)}" 
   return result
# reuseable function to display result template ends

#? perfom the user calculation
#todo: this function will add the two provided numbers
def add(value1, value2): 
    #Print return result msg template!
    print(f"\n {displayResult(user, int(value1 + value2))}")

#todo: this function will subtract the two provided numbers
def subtract(value1, value2): 
    #Print return result msg template!
    print(f"\n {displayResult(user, int(value1 - value2))}")

#todo: this function will divide the two provided numbers
def divide(value1, value2):
    #Print return result msg template!
    print(f"\n {displayResult(user, int(value1 / value2))}")

#todo: this function will multiply the two provided numbers
def multiply(value1, value2):
    #Print return result msg template!
    print(f"\n {displayResult(user, int(value1 * value2))}")

#? PROCESS THE CALCULATION BASED ON THE USER'S OPERATION
#todo: IF USER OPERATES TO ADD
if operation == "plus": add(number1, number2) 
    
#todo: IF USER OPERATES TO SUBTRACT
elif operation == "minus": subtract(number1, number2) 

#todo: IF USER OPERATES TO DIVIDE
elif operation == "divide": divide(number1, number2)

#todo: IF USER OPERATES TO MULTIPLY
elif operation == "multiply": multiply(number1, number2)

#todo: IF USER ENTERS ANY THING OTHER THAN THE ABOVE OPERATIONS
else:  print("\n Oops, something went Wrong, Seems you didn't follow the intruction! Try Again.")


#? Lol
print("\n Thanks for using our App!")