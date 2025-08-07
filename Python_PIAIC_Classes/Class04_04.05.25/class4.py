
def greet():
  print("Hello World")

greet()

# ------------------------------------------------

def sum( num1, num2 ):
  print(num1 + num2)

sum( num1 = 5, num2 = 10 )
sum( 5, 10 )

# ------------------------------------------------

def calculator(num1, num2, operator):
  if operator == '+':
    print(num1 + num2)
  elif operator == '-':
    print(num1 - num2)
  elif operator == '*':
    print(num1 * num2)
  elif operator == '/':
    print(num1 / num2)
  else:
    print("Invalid Operator")

num1 = int(input('Enter your first number'))
operator = input('Enter your operator')
num2 = int(input('Enter your second number'))

calculator(num1,num2 ,operator)

# calculator(2,2,'+')
# calculator(2,2,'*')
# calculator(2,2,'/')

# ------------------------------------------------

def greet(age, name = "User"):
  print(f'Hello {name} and you are {age} years old')

greet(21, "Okasha")
greet(21)