
# =============================================
# Add Types in Functions (Type Hints)
# =============================================

# def greet(name: str) -> str:
#   return(f'Hello {name}')

# print(greet('Ali'))


# =============================================
# Dictionaries (key-value pairs)
# =============================================

stu_details = {
  'name': 'sajid',
  'age': 45,
  'address': 'Karachi'
}

print(stu_details) # {'name': 'sajid', 'age': 45, 'address': 'Karachi'}
print(stu_details['name']) # sajid
print(stu_details['age']) # 45
print(stu_details['address']) # Karachi


# =============================================
# How to use Dictionaries (key-value pairs) in f-String?
# =============================================

print(f'''
Name = {stu_details['name']}
Age = {stu_details['age']}
Address = {stu_details['address']}''')


