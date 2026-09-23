#Python tutorial
10 #numbers
"Hello" #string
True #boolean
print("Hello World") #string (sequence of characters)

#variables
age = 20
print(age)

#change variable
age = 30
print(age)

price = 19.95
first_name = "Luisa" #use underscore
is_online = True #boolean (case sensitive)

#Exercise 1
first_name = "John"
last_name = "Smith"
age = 20
new_patien = True

#input function
name = input("What is your name? ") #Returns value in brackets
print("Hello " + name) #string concatenation

birth_year = input("Enter your birth year: ") #string
#age = 2026 - birth_year #integer
# print(age) creates an error because you cannot subtract a string from an integer
#convert string into integer:
age = 2026 - int(birth_year)
print(age)

#convert value to xy:
int()
float() #floating point number (decimal)
bool()
str()

#Exercise 2:
first_number = input("Enter your first decimal number: ")
second_number = input("Enter your second decimal number: ") #input creates string, so we need to convert it into a float first
print("The sum of your numbers is " + str(float(first_number) + float(second_number)))

#strings in python
course = "Python for Beginners" #string object
print(course.upper()) #string methods, returns new string
print(course) #course not affected
print(course.find("y")) #index of first character
print(course.find("Y")) #case sensitive
print(course.replace("for", "4")) #does not modify original string
#strings are immutable
print(course.find("Python"))
print("Python" in course) #in operator, returns boolean

#arithmetic operators (same as in math)
print(10+3)
print(10*3)
print(10-3)
print(10/3) #decimal
print(10//3) #integer
print(10%3) #remainder of division
print(10**3) #potence

x = 10
x = x+3 #stores 13 in x
# x+=3 is exactly identical to the line above
print(x)

#operator precedence
x = 10+3*2 #=16
y = (10+3)*2 #=26

print(x)
print(y)

#comparison operators
x = 3 > 2 #returns boolean True
print(x)

y = 3>=2
z = 3==2 #== (comparison)not the same as = (assignment)
print(y)
print(z)

v = 3!=2 #not equal
print(v)

#logical operators
price = 25
print(price > 10 and price < 30) #if both true, returns true
print(price > 30 or price < 40) #if at least one is true, returns true

price = 5
print(price >10)
print( not price >10)

#if statements
temperature = 11
if temperature > 30: #indented: block of code
    print("It's a hot day!") #executed if condiiton is True
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day!") #(20, 30)
elif temperature > 10:
    print("It's a bit chilly!")
else: #is executed if none of the above is True
    print("It's a cold day!")
print("Done") #not indented, always executes

#Exercise 3
weight = input("What is your weight? ")
unit= input("Is your weight in kg or lbs? ")
if unit.lower() == "kg":
    print("Weight in kg: " + weight)
else:
    print("Weight in lbs: " + weight)

#while loops
i = 1
while i <= 5:
    print(i)
    i = i + 1 #without this line, i will remain 1 and will not stop

i = 1
while i <= 10:
    print(i*'*')
    i = i + 1

#lists
names = ["Michael", "David", "Maria", "James"]
print(names)
print(names[0])
print(names[-1]) #last element in list

names[0] = "Michel" #change value in list
print(names)

print(names[1:3]) #value at index 3 excluded, expression does not modify our list

#list methods (lists are objects)
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

numbers.insert(0,-1)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4, 5]
print(1 in numbers) #returns boolean

print(len(numbers))

#for loops
numbers = [1,2,3,4,5]
for number in numbers: #version with for loop shorter than with while
    print(number)

i = 0
while i<len(numbers):
    print(numbers[i])
    i = i+1

#range() function
numbers = range(5) #returns sequence of numbers excluding 5
print(numbers)

for i in numbers: #to see all numbers, use for loop
    print(i)

numbers = range(5, 10) #5-9
for i in numbers:
    print(i)

numbers = range(5, 10, 2) #every other number
for i in numbers:
    print(i)

for number in range(5):
    print(number)

#tuples (immutable)
numbers = (1, 2, 3, 3) #tuple

print(numbers.index(2))
print(numbers.count(3))