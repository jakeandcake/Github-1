import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y): 
    return x * y
def divide(x, y):
    return x / y
def exponent(x, y):
    return x ** y
def square(x):
    return math.sqrt(x)
def sine(x):
    return math.sin(x)
def cosine(x):
    return math.cos(x)
def tangent(x):
    return (math.sin(x)/math.cos(x))
def cotangent(x):
    return (math.cos(x)/math.sin(x))
def cosecant(x):
    return (1/math.sin(x))
def secant(x):
    return (1/math.cos(x))

def numcheck(x):
    while True:
        try:
            x = int(x)
            return int(x)
        except:
            x = input("Enter another number: ")
            continue
def opcheck(user_op):
    valid_op = ["+", "-", "*", "/", "^", "sqrt", "sin", "cos", "tan", "cot", "csc", "sec"]
    while True:
        if user_op in valid_op:
            return user_op
        else:
            user_op = input("Enter another operator: ")
def divisionzero(user_op, y):
    #y stands for the second number and checks for division by zero
    #This returns a new second number if previous isn't valid
    while True:
        if user_op == "/" and y == 0:
            print("Cannot divide by 0")
            y = input("Enter another number to divide with: ")
            while True:
                try:
                    y = int(y)
                    break
                except:
                    y = input("Enter a valid number")
        else:
            return y

def results(x, y, user_op):
    #utilizes functions, prints results
    while True:
        if user_op == "+":
            print(add(num0, num1))
            break
        elif user_op == "-":
            print(subtract(num0, num1))
            break
        elif user_op == "*":
            print(multiply(num0, num1))
            break
        elif user_op == "/":
            print(divide(num0, num1))
            break
        elif user_op == "^":
            print(exponent(num0, num1))
            break
        elif user_op == "sqrt":
            print(square(num0))
            break
        elif user_op == "sin":
            print(sine(num0))
            break
        elif user_op == "cos":
            print(cosine(num0))
            break
        elif user_op == "tan":
            print(tangent(num0))
            break
        elif user_op == "cot":
            print(cotangent(num0))
            break
        elif user_op == "csc":
            print(cosecant(num0))
            break
        elif user_op == "sec":
            print(secant(num0))
            break
    return 0

#Gets user inputs
single_digit_ops = ["sin", "cos", "tan", "cot", "csc", "sec"]
num0 = input("Enter your first number: ")
num0 = numcheck(num0)
print("Note some operators don't have a symbol, just enter the letter equivalent")
op = str(input("Enter the symbol for your operator: "))
op = opcheck(op)
if op in single_digit_ops:
    num1 = None
else:
    num1 = input("Enter your second number: ")
    num1 = numcheck(num1)
    num1 = divisionzero(op, num1)

results(num0, num1, op)
