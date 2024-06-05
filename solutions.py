#ASSIGNMENT SUBMISSION
#STUDENT NAME- IVY MBENGI 



#1. Python Basics:
 #  - What is Python, and what are some of its key features that make it popular among developers? Provide examples of use cases where Python is particularly effective.

#Solution:
#Python is a high-level, interpreted programming language that is widely used for many different purposes, from web development to scientific computing to machine learning.

#Key features:
#Simple and Readable Syntax: Python's syntax is clear and easy to understand, making it an excellent language for beginners.
#Dynamic Typing: Python is dynamically typed, which means you don't need to declare the type of a variable when you create one.
#Interpreted Language: Python code is executed line-by-line, which makes debugging easier.
#Extensive Standard Library: Python has a large standard library that supports many common programming tasks.
#Support for Multiple Paradigms: Python supports procedural, object-oriented, and functional programming styles.
#Community and Libraries: Python has a vast community and a rich ecosystem of third-party libraries and frameworks.


#2. Installing Python:
#   - Describe the steps to install Python on your operating system (Windows, macOS, or Linux). Include how to verify the installation and set up a virtual environment.

#For Windows:

#Download Python Installer by going to the Python website and downloading the latest installer for Windows.
#Run the Installer by executing the installer and making sure to check "Add Python to PATH" before clicking "Install Now."
#Verify Installation: Open Command Prompt on your computer and type python --version to check the installed version.
#Install venv that comes with Python by default.
#Create a virtual environment by running the command python3 -m venv {myenv} where {myenv} is the name of your environment.
#Activate the Environment by running the following command: {myenv}\Scripts\activate



# 3. Python Syntax and Semantics:
#    - Write a simple Python program that prints "Hello, World!" to the console. Explain the basic syntax elements used in the program.


print("Hello, World!")
#print is a function that outputs texts to the console
#The text to be printed out is put within the brackets in quotation marks
#Hello, World is considered a string, which is a series of characters


# 4. Data Types and Variables:
#    - List and describe the basic data types in Python. Write a short script that demonstrates how to create and use variables of different data types.

# Basic Data Types:

# -Integer (int): Whole numbers, e.g., 1, -5, 42.
# -Float (float): Numbers with a decimal point, e.g., 3.14, -0.001.
# -String (str): Sequence of characters, e.g., "hello", 'world'.
# -Boolean (bool): Logical values, True or False.
# -List (list): Ordered, mutable(can be changed) collection of items, e.g., [1, 2, 3].
# -Tuple (tuple): Ordered, immutable(cannot be changed) collection of items, e.g., (1, 2, 3).
# -Dictionary (dict): Unordered collection of key-value pairs, e.g., {'name': 'Alice', 'age': 25}.

# Integer
age = 25
#Float
pi=3.14159
#String
name="Alice"
#Boolean
is_student=True
#List
animals=["dog","cat","horse","ferret"]
#Tuple
coordinates=(10.0, 20.0)
#Dictionary
person={
    "name":"Jerry",
    "age": 25,
    "is_student": False,    
    }
print(f"My friend {name}, who is {age} years old, is {'a student' if is_student else 'not a student'}.
       They have a pet {animals[0]} living with them at their home located at coordinates ({coordinates[0]}, 
       {coordinates[1]}). Here's some fun fact for {name}, the value of pi is approximately {pi}.")


# 5. Control Structures:
#    - Explain the use of conditional statements and loops in Python. Provide examples of an `if-else` statement and a `for` loop.

#Conditional statements introduce conditions such that the code runs only when the condition is met, otherwise it fails to run.
#Loops introduce iteration to code for pieces of code that require to run a certain number of times more than one

x = 10
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

   
# 6. Functions in Python:
#    - What are functions in Python, and why are they useful? Write a Python function that takes two arguments and returns their sum. Include an example of how to call this function.

# Functions are reusable pieces of code that perform a specific task

def add_numbers(a, b):
    return a + b

# Calling the function
result = add_numbers(3, 5)
print("Sum:", result)

# 7. Lists and Dictionaries:
#    - Describe the differences between lists and dictionaries in Python. Write a script that creates a list of numbers and a dictionary with some key-value pairs, then demonstrates basic operations on both.

# A list is an ordered collection of items that is accessed by index. A dictionary is an unordered collection of key-value pairs that are accessed by keys.

# List
numbers.append(6)
print("Numbers:", numbers)
print("First number:", numbers[0])

# Dictionary
person = {
    "name": "Alice",
    "age": 25
}
person["age"] = 26
person["city"] = "New York"
print("Person:", person)
print("Name:", person["name"])


# 8. Exception Handling:
#    - What is exception handling in Python? Provide an example of how to use `try`, `except`, and `finally` blocks to handle errors in a Python script.


# Exception handling is an event that allows you to manage and respond to runtime errors in your program  without crashing.

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("This will always execute")


# 9. Modules and Packages:
#    - Explain the concepts of modules and packages in Python. How can you import and use a module in your script? Provide an example using the `math` module.

# Module: A file containing Python code which can define functions, classes, and variables.
# Package: A collection of modules organized in directories that include a special __init__.py file.

import math

# Using functions from the math module
print("PI:", math.pi)
print("Square root of 16:", math.sqrt(16))


# 10. File I/O:
#     - How do you read from and write to files in Python? Write a script that reads the content of a file and prints it to the console, and another script that writes a list of strings to a file.

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


strings = ["Hello", "World", "This", "is", "Python"]

with open('example.txt', 'w') as file:
    for line in strings:
        file.write(line + "\n")





