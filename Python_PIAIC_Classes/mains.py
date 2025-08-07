# *************************************************
#                   PYTHON PRACTICE
# *************************************************

# =================================================
# float() method:
# =================================================
# num = 78
# print(float(num)) # 78.0

# =================================================
# Multiline Comments:
# =================================================
# '''my name is Sajid Hanif and
# I am learning Python
# from PIAIC'''

# =================================================
# Multiline String:
# =================================================
# comments = '''my name is Sajid Hanif and
# I am learning Python
# from PIAIC'''

# print(comments)

# =================================================
# ID & Type Methods:
# =================================================
# print(id(comments)) # 1812771021280

# print(type(comments)) # <class 'str'>

# print(type(comments) == str) # True

# =================================================
# isdigit Method:
# =================================================
# user_age = input('Enter your age:')

# if user_age.isdigit():
#     print(f'You age is {user_age}' )
# else:
#     print('Enter your age in digits')



fruits: list = ['banana', 'grapes', 'orange', 'mango']

# print(fruits)
# fruits.append('apple')
fruits.extend(['apple', 'dates', 'strawbery'])
print(fruits)

# fruits.remove('banana')

# fruits.sort()
# print(fruits)
# fruits.sort(reverse=True)
# fruits.reverse()
# print(fruits)
# fruits.sort(key=len)
# print(fruits)


for fruit in fruits:
    print(fruit)














