# *************************************************
#                Class11_29.06.25
# *************************************************

# def check_age(age: int) -> bool:
#     print('check age function is called')

# check_age('18') # For error, mypy package is to be installed.
# check_age(18)

# ==================================================

# def check_age(age: int) -> bool:
#     pass # nothing to do (None)

# check_age(18)

# ==================================================

# def check_age(age: int) -> bool:
#     pass # nothing to do (None)

# result = check_age(18) # None


# ==================================================

# def is_age_valid(age: int) -> bool:
#     if age > 18:
#         return True
#     else:
#         False

# result = is_age_valid(18) # None

# ==================================================

# def is_age_valid(age: int) -> bool:
#     if age > 18:
#         return True
#     else:
#         return False

# print ( is_age_valid(18)) # False

# ==================================================

# name = 'Hamza'
# print(id(name))
# name = 'Ali' # Creates a new vatiable with the same name with new id.

# print(name) # Ali

# name[0] = 'a'
# print(name) # Immutable

# NOTE: String is Immutable.

# ==================================================
#                   Interning
# ==================================================

# name1 = 'Ali'
# name2 = 'Ali'

# print(id(name1)) # Same id
# print(id(name2)) # Same id

# NOTE: If values are same, locations/ id will also be same.

# ==================================================

# name1 = 'Ali'
# name2 = 'ali'

# print(id(name1)) # Different id
# print(id(name2)) # Different id

# ==================================================
#                       Set
# ==================================================
# Unordered, Mutable, Unique values

# roles = {'Admin', 1, 2, 4, 'Hello World', 4, 2, 1}

# print(roles)

# roles.add('Ali') # it will be added because Set is Immutable
# print(roles)

# roles.remove('Admin') # it will be removed because Set is Immutable
# print(roles)

# NOTE: Only premitive data type values can be added in Set, but Immutable type data cannot be added. 

# ==================================================

# traffic_light: frozenset = frozenset ( {'red', 'orange', 'green'} )

# NOTE: frozenset cannot be changed, because it is Immutable

# =========================================================
# IMMUTABLE IS MORE EFFICIENT (FAST) AS COMPARE TO MUTABLE
# =========================================================

# val = {}

# print( type (val) ) # <class 'dict'>


# Q. What are mutable and immutable in Python?
# Q. Pass by value and Pass by reference?

# =========================================================
#               Short Hand of If Condition
# =========================================================

# age = 18
# result = 'You are allowed' if age >= 18 else 'You are not allowed'
# print(result)


# =========================================================
#                        OOPs 
# =========================================================

# How to create Class?

class House:
    def __init__(self): # __init__ is a constructor
        # self = {}, self is an empty object 
        self.address = 'XYZ 123'
        # self = { address: XYZ 123}
        self.number_of_rooms = 4
        # self = { address: XYZ 123, number_of_rooms: 4}
        self.number_of_doors = 2
        # self = { address: XYZ 123, number_of_rooms: 4, number_of_rooms: 2}

h1 = House() # to create an object h1
# print(h1.address) # XYZ 123

h2 = House()
# print(h2.address) # XYZ 123

# =========================================================

class House:
    def __init__(self, addrs): # __init__ is a constructor
        self.address = addrs
        self.number_of_rooms = 4
        self.number_of_doors = 2

h1 = House('A29') # to create an object h1
# print(h1.address) # A29

h2 = House('A30')
# print(h2.address) # A30


# =========================================================

class House:
    def __init__(self, addrs): # __init__ is a constructor
        self.address = addrs
        self.number_of_rooms = 4
        self.number_of_doors = 2

    def ring_bell(self):
        print('Ding Dong')

h1 = House('A29') # to create an object h1
print(h1.address) # A29

h1.ring_bell()

# =========================================================

class Apartment(House):
    def __init__(self, addrs, flat_num):
        super().__init__(addrs)
        self.flat_number = flat_num

apart1 = Apartment('Abc', 23)        
print(apart1.address)
print(apart1.number_of_rooms)
print(apart1.number_of_doors)
print(apart1.flat_number)


