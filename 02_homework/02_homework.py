#notes video "Python Full Course for Beginners"
#syntax => grammar of programming

print("Hello, World")
print("*"*10)

#Python Extensions
#Convert Editor to IDE by using extension python
#linting: analysing code for errors
#debuggin: fixing errors
#autocompletion: faster coding
#code formatting: clean, readable code
#unit testing: test code to behave correctly
#code snippets

#LINTING CODING
# invalid code: print "Hello, World"
#see potential errors in code

#invalid syntax: 2+ 

#problems panel (Cmd + Shift + m): all problems from code
#command palette (Cmd + Shift + p)

#FORMATTING CODE
#Python Enhancement Proposals (PEPs):
#Each Pep has a number and a title.
#Popular: P8 (Style Guide for Python Code)

x=1
#P8: "ugly code", no spaces
#automatically format code: pep8

#format code automatically possible 

#RUNNING PYTHON CODE
#in terminal: python3 xy (if do not have access to code editor)
#play button
#simplest way: shortcut (create it yourself, i chose ctrl+r)

#PYTHON IMPLEMENTATION
#default implementation: CPython

#HOW PYTHON CODE IS EXECUTED
#Compiler: convert code to machine code
#Java: compiles into portable language (Java Bytecode)
#JVM: convert Java Bytecode into Machine Code
#Python => CPython => Python Bytecode => PVM => Machine Code

#VARIABLE Names
#descriptive and meaningful
#use underscore to separate words
#lower case letters
#space around "="

#STRINGS
#tripple string: to format string
message = """
Hello
"""

#function: reusable piece of code
#some functions take arguments/inputs

#ESCAPE SEQUENCE

#course = "Python "Programming" (invalid)
#solution: 'Python "Programming'
#or: "Python \"Programming"
#\ escape character
#\" escape sequence
#\'
#\\
#\n: paragraph

#FORMATTING STRINGS
first = "Mosh"
last = "Hamedani"
full = first + " " + last
print(full)

full = f"{first} {last}" #any valid expression inbetween curly braces
print(full)

#STRING METHODS
course = " python Programming"
#everything in python is an object, objects have methods, use dot-notation to access its methods

print(course.upper()) #original string is not affected
print(course.title())
print(course.strip()) #white spaces removed
print(course.lstrip())
print(course.rstrip())
print(course.find("p"))
print(course.replace("p", "j"))
print("pro" in course) #expression, produces value
print("pro" not in course)

#NUMBERS
#i is imaginary number
#instead of i use j for complex number

x = 1+2j

#augmented assignment operator
x = 10
x = x + 3
x += 3

#WORKING WITH NUMBERS

import math #(math is object)
print(round(2.9))
print(abs(-3.9))

print(math.ceil(2.2))

#find complete list: python 3 math module

#TYPE CONVERSION

x = input("x: ")
#y = x + 1 cannot add string to number

#built-in functions
#int(x)
#float(x)
#bool(x)
#str(x)

print(type(x))

y = int(x) +1
print(f"x: {x}, y: {y}")

#truthy and falsy values
#Falsy: "", 0, None (absence of value)

#CONDITIONAL STATEMENTS
temperature = 23
if temperature > 30:
    print("It is warm")
    print("Dring water")
elif temperature > 20:
    print("It is nice")
else:
    print("It is cold.")
print("Done") #always executed regardles of condition

#TERNARY OPERATOR
age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible") #not false code

#better: 
age = 12
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

message = "Eligible" if age >= 18 else "Not eligible" #equivalent to above, much shorter
print(message)

#LOGICAL OPERATORS
#and, or, not

high_income = True
good_credit = True
student = True

if high_income and good_credit: #do not need to add == True
    print("Eligible")
else:
    print("Not eligible")

if not student:
    print("Eligible")
else:
    print("Not eligible")

if (high_income or good_credit) and not student:
    print("Eligible")

    #SHIRT_CIRCUIT EVALUATION
high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")

#CHAINING COMPARISON OPERATORS
#age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("Eligible")

#or chaining:
if 18 <= age < 65:
    print("Eligible")

#FOR LOOPS
for number in range(3):
    print("Attempt", number + 1)

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, (number + 1) * ".")

#FOR ELSE
successful = False
for number in range(3):
    print("Attempt", number)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

#NESTED LOOPS
for x in range (5):
    for y in range(3):
        print(f"({x}, {y})")

#ITERABLES
print(type(5)) #int

print(type(range(5))) #type range object, complex types

#iterable objects: range, string, list

for x in "Python":
    print(x)

for x in [1, 2, 3, 4, 5]:
    print(x)

shopping_cart = ["shoes", "tomatoes"]
for item in shopping_cart:
    print(item)

#WHILE LOOPS
number = 10
while number > 0:
    print(number)
    number //= 2

#command = ""
#while command != "quit":
    #command = input(">")
    #print("ECHO", command)

while True:
    command = input(">")
    if command.lower() == "quit":
        break

#QUIZ

range(1, 10)

count = 0
for number in range(1, 10):
    if number%2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")

#FUNCTIONS
def greet():
    print("Hi, there")
    print("Welcome aboard")


greet()

def greet(first_name, last_name):
    print(f"Hi, {first_name} {last_name}.")
    print("Welcome aboard")

greet("Luisa", "Schnabel")

#TYPES OF FUNCTIONS
#1: perform a task
#2: return a value


def get_greeting(name):
    return (f"Hi, {name}")

message = get_greeting("Luisa")
#we can do whatever with message variable
#all functiosn, by default, return None object if you do not return something else

#KEYWORDS ARGUMENT
def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)
#or
print(increment(2,1))
#keyword arguments:
print(increment(number=2, by=1))

#DEFAULT ARGUMENTS
def increment(number, by=1): #default value by=1
    return number + by


print(increment(number=2))

#arg, …

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5)) #tuples are iterable