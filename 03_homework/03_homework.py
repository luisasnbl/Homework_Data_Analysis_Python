#notes video "Python for Beginners - Learn Coding with Python in 1 Hour"
##variables
#remember: python is case sensitive

##input

name = input("What is your name? ")
print("Hello " + name) #string concatenation

#Type Conversion
birth_year = input ("Enter your birth year: ")
#age = 2020 - birth_year would create error (integer - string)
#instead:
age = 2026 - int(birth_year)
print(age)

first = input("First: ")
second = input("Second: ")
sum = float(first)+float(second)
print(sum)

#Strings
course = "Python for Beginners" #object with many capabilities
print(course.upper()) #specific functions (methods)
print(course) #string is not affected
print(course.find("y"))
print(course.find("Y")) #case sensitive
print(course.replace("for", "4"))
print("Python" in course)

weight = input("How much do you weigh? ")
metric = input("Is this weight in Kg or Lbs? ")

if metric.lower() == "kg":
    print("Weight in kg: ", weight)
else:
    print("Weight in kg: ", float(weight)*1.6)

#While loops
i = 1
while i <= 5:
    print(i * "*")
    i += 1

#lists
names = ["Luisa", "Amelie", "Domenica"]
print(names[0])
print(names[-1])

names[0] = "Lotti"
print(names)
print(names[0:2])

#list methods
#lists are also objects
numbers = [1, 2, 3, 4, 5, 6]
numbers.insert(6, -1)
print(numbers)
print(1 in numbers)
print(10 in numbers)
print(len(numbers))

#for loops
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number)

#range function
numbers = range(5)
print(numbers)

for number in numbers:
    print(number)

numbers = range(5, 10, 2)
for number in numbers:
    print(number)

for number in range(3, 14):
    print(number)

