# *********************************************************************************
# Class No. 01 - 17.12.24
# Python Fundamentals for AI in Google Colab
# *********************************************************************************


# *********************************************************************************
# Class No. 02 - 24.12.24
# Mastering Strings, F-Strings, Arithmetic & Assignments in Python!
# *********************************************************************************


# *********************************************************************************
# Class No. 03 - 31.12.24 
# Mastering Boolean, Comparison Operators, Logical Operators and If-else in Python!
# *********************************************************************************

# =================================================================
# If statement:
# =================================================================
# is_hungry = True
# burger_lover = True
# pizza_lover = False

# if ( is_hungry and (burger_lover or pizza_lover) ):
#     print("Let's order the Food")
# else:
#     print('No need to orde Food')



# *********************************************************************************
# Class No. 04 - 07.01.25
# What are Lists in Python? List Methods in Python
# *********************************************************************************

# =================================================================
# List Methods:
# =================================================================
# Shopping List
# shopping_list : list[str] = ['Cake', 'Eggs', 'Juice', 'Chips', 'Bread']
# print(shopping_list)

# =================================================================
# append() method: Adds the item in the last
# =================================================================
# shopping_list.append('Flour')
# print(shopping_list)

# =================================================================
# pop() method: Removes the item from the last
# =================================================================
# shopping_list.pop()
# print(shopping_list)

# shopping_list.pop(3)
# print(shopping_list)

# =================================================================
# insert() method: Inserting item in the list
# =================================================================
# shopping_list.insert(3, 'Chocolate')
# print(shopping_list)

# =================================================================
# remove() method: Removing item in the list
# =================================================================
# shopping_list.remove('Eggs')
# print(shopping_list)



# *********************************************************************************
# Class No. 05 - 14.01.25 
# What are functions in Python. How to write Functions
# *********************************************************************************
# print('Hello Sajid')

# =================================================================
# Function Example:
# =================================================================
# def greet(name):
#   print(f'Hello {name}')

# greet('Asif') # Hello Asif
# greet('Arif') # Hello Arif
# greet('Huzaifa') # Hello Huzaifa


# =================================================================
# Function with return Keyworkd:
# =================================================================
# def sum(a,b):
#   c = a + b
#   return c

# res = sum(5,2)
# print(res) # 7

# =================================================================
# Function with default value:
# =================================================================
# def greet(user_name = 'Guest'):
#     print(f'Welcome! {user_name}')

# greet('Sajid') # Welcome! Sajid
# greet() # Welcome! Guest

# =================================================================
# Calculator with User Inputs:
# =================================================================
# num1 = int(input('Enter number: '))
# opr = input('Select Opr (+ - * /): ')
# num2 = int(input('Enter number: '))

# if (opr == '+'):
#     print(num1 + num2)
# elif (opr == '-'):
#     print(num1 - num2)
# elif (opr == '*'):
#     print(num1 * num2)
# elif (opr == '/'):
#     print(num1 // num2)
# else:
#     print('Enter valid number')

# =================================================================
# Calculator with Function:
# =================================================================

# def calc(num1, num2, opr):
#     if (opr == '+'):
#         print(num1 + num2)
#     elif (opr == '-'):
#         print(num1 - num2)
#     elif (opr == '*'):
#         print(num1 * num2)
#     elif (opr == '/'):
#         print(num1 // num2)
#     else:
#       print('Invalid operator')

# calc(2, 5, '+') # 7
# calc(20, 5, '-') # 15
# calc(22, 2, '*') # 44
# calc(225, 5, '/') # 45


# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# print( dir(items) )


# *********************************************************************************
# Class No. 06 - 21.01.25 
# Dictionary in Python. Why we need dictionary? Loops in Python. For & While Loops
# *********************************************************************************

# =================================================================
# Dictionaries:
# =================================================================
# users: dict = {
#     'username': 'Sajid',
#     'age': 45,
#     'city': 'Karachi'
# }

# print(type(users)) # <class 'dict'>

# =================================================================
# Updating values in a Dictionary:
# =================================================================
# users['username'] = 'Huzaifa'
# print(users['username'])

# users['age'] = 26
# print(users['age'])

# users['city'] = 'Islamabad'
# print(users['city'])

# =================================================================
# Adding values in a Dictionary:
# =================================================================
# users['Country'] = 'Pakistan'

# print(users) # {'username': 'Huzaifa', 'age': 26, 'city': 'Islamabad', 'Country': 'Pakistan'} 


# =================================================================
# For Loop:
# =================================================================

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# For loop Example 01:
# for i in range(1,6):
#     print(i)


# For loop Example 02:
# students = ['sajid', 'huzaifa', 'hamza', 'asif', 'arif']

# for name in students:
#     print(name)


# While Loop:
# countdown = 10
# while countdown > 0:
#     print(countdown)
#     countdown -= 1


# Guess the Number:
# correct_number = 9
# guess_number = 0

# while guess_number != correct_number:
#     guess_number = int(input('Guess the number: '))
#     print('Wrong! Try again please.' if guess_number != correct_number else 'Wow! You guess it right')




# a = 'this is a very long string this is a very long string'
# b = 'this is a very long string this is a very long string'

# print(a is b)
# print(id(a))
# print(id(b))

a = "12345678901234567890"
b = "12345678901234567890"
print(a is b) 















