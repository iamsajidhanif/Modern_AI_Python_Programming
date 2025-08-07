
# id method:
# first_name = 'Hamza'
# print(id(first_name)) # 2545478445760

# type method:
# print(type(first_name)) # <class 'str'>

# Comparision Opr (==):
# print (type(first_name) == str) # True

# Age Datatype Checking:
# age = input('Enter your age: ')
# if age.isdigit():
#     print(age.isdigit()) # returns True
#     print(age)
# else:
#     print('Please enter age in digits')

# Emojis Shortcut: Win + .

# ------------------------------------------------------
# If Statement with Logical Opr
# ------------------------------------------------------
# bobzi_runs = 50

# if bobzi_runs >= 50:
#     print('Real King')
# else:
#     print('Dummy King')

# ------------------------------------------------------

# bobzi_runs = 50
# total_balls = 20

# if bobzi_runs >= 50 and total_balls < bobzi_runs:
#     print('Real King')
# else:
#     print('Dummy King')

# ------------------------------------------------------

# bobzi_runs = 36
# total_balls = 20
# total_sixes = 5

# if bobzi_runs >= 50 and total_balls < bobzi_runs or total_sixes >= 5:
#     print('👍 King')
# else:
#     print('🔔 King')

# ------------------------------------------------------

# List (for multple values):
items = ['Hara dhaniya', 'Podina', 'Dahi', 'Eggs']

# print(items) # ['Hara dhaniya', 'Podina', 'Dahi', 'Eggs']

# print(items[2]) # Dahi

# print(items[2], items[3]) # Dahi Eggs

# -------------------------------------------------------------

# print(type(items)) # <class 'list'>

# -------------------------------------------------------------

# print(len(items)) # 4

# -------------------------------------------------------------

# print(dir(items)) # shows functions related to items(list)

# -------------------------------------------------------------

# items.pop() # remove last item of the list
# print(items)

# -------------------------------------------------------------

# items.append('Roti')  # add items at the last
# print(items)

# -------------------------------------------------------------

# items.insert(2, 'Roti')  # add items at specific indext
# print(items)

# print(f'{items[0]}, {items[1]}') # Hara dhaniya, Podina

# -------------------------------------------------------------

# items.remove('Podina')  # removes item from the list
# print(items)