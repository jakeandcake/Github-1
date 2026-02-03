#Side notes: Make division by 0 print statement valid when asking for another valid operator
#Make it so it asks for valid operator again if it doesn't work
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

num0 = input("Enter your first number: ")
print("Note some operators don't have a symbol, just enter the letter equivalent")
op = str(input("Enter the symbol for your operator: "))
print(op)
if op == "sin" or op == "cos":
    num1 = 0
else:
    num1 = input("Enter your second number: ")
while True:
    try:  
        while True: #loop that asks for num0 input if invalid
            try:
                num0 = int(num0)
                break
            except:
                num0 = input("Enter a valid number\n")
                continue
        if int(num1) == 0 and op == "/": #checks for division by 0
            print("Cannot divide by 0") 
            num1 = num0 / num1 #triggers except block
        num1 = int(num1)
        break
    except:
        num1 = input("Enter a valid number: ") #asks for num1 input if invalid
        continue
#print(type(num0), type(num1)) - If you wanted to test the types
while True: #utilizes functions and asks for input for operator if invalid.
    if op == "+":
        print(add(num0, num1))
        break
    elif op == "-":
        print(subtract(num0, num1))
        break
    elif op == "*":
        print(multiply(num0, num1))
        break
    elif op == "/":
        print(divide(num0, num1))
        break
    elif op == "^":
        print(exponent(num0, num1))
        break
    elif op == "sqrt":
        print(square(num0))
        break
    elif op == "sin":
        print(sine(num0))
        break
    elif op == "cos":
        print(cosine(num0))
        break
    elif op == "tan":
        print(tangent(num0))
        break
    elif op == "cot":
        print(cotangent(num0))
    elif op == "csc":
        print(cosecant(num0))
    elif op == "sec":
        print(secant(num0))
    
    else:
        op = str(input("Enter a valid operator: "))
        if int(num1) == 0 and op == "/": #checks for division by 0
            print("Cannot divide by 0")
        
        
