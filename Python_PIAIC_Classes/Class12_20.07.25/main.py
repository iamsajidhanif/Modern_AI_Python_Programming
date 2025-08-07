# *************************************************
#                Class12_20.07.25
# *************************************************

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

h2 = House('A30') # A30 is a positional argument
# print(h2.address) # A30

h3 = House(addrs = 'A35') # A35 is a keyword argument
# print(h2.address) # A30

# =========================================================

class House:
    def __init__(self, addrs): # __init__ is a constructor
        self.address = addrs
        self.number_of_rooms = 4
        self.number_of_doors = 2

    def ring_bell(self):
        print('Ding Dong')

    def call_lift(self):
        print(f'{self.address} Lift is called')

h1 = House('A29') # to create an object h1
print(h1.address) # A29

h1.ring_bell()

h1.call_lift() # A29 Lift is called


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

# =========================================================
#                       Task No. 01
# =========================================================

class Student:
    def __init__(self, roll_number, stu_name): # __init__ is a constructor
        self.roll_number: int = roll_number
        self.stu_name: str = stu_name

    def pay_fee(self):
        print(f'The roll No.{self.roll_number}, Mr. {self.stu_name} has paid the fee')

    def get_admission(self):
        print(f'The roll No.{self.roll_number}, Mr. {self.stu_name} has got the admisssion')

stu1 = Student(1234, 'Huzaifa')
print(stu1.roll_number, stu1.stu_name) # 1234 Huzaifa

stu1.pay_fee() # 1234 Huzaifa has paid the fee
stu1.get_admission() # The roll No.1234, Mr. Huzaifa has got the admisssion

class Course:
    def __init__(self, course_name):
        self.course_name: str = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

ai_course = Course('AI')
print(ai_course.students)

ai_course = Course('AI')
ai_course.add_student(stu1)
print(ai_course.students[0].stu_name)

# =====================================================================
#                           1. Inheritance 
# =====================================================================

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eating with right hand')


class Student(Human):
    def __init__(self, name, age, rolNum):
        super().__init__(name, age)
        self.rolNum = rolNum

stu11 = Student('Sajid', 21, 13245)
print(stu11.name)
print(stu11.age)
print(stu11.rolNum)

print(stu11.name, stu11.age, stu11.rolNum)

# =====================================================================
#                           2. Polymorphism  (Overriding) 
# =====================================================================

class Teacher(Human):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salry = salary

    # Polymorphism (Overriding)
    def eat(self):
        print('eating with left hand')

teacher1 = Teacher('Okasha', 28, 50000)

print(teacher1.name)
print(teacher1.eat())

# =====================================================================
#                           3. Encapsulation
# =====================================================================

# 1. Public Properties/ Attributes
# 2. Private Properties/ Attributes (double underscore)
# 3. Protected Properties/ Attributes (single underscore)

class BankAccout():
    def __init__(self, name, account_no, balance):
        self.name = name
        self._account_no = account_no # we make a property as "Protected" with "single underscore"
        self.__balance = balance # we make a property as "Private" with "double underscore" 
    
    def get_balance(self, account_no): # getter method
        if self.account_no == account_no:
            return self.__balance
        else:
            return "Invalid account number"

user1 = BankAccout('Okasha', 123456, 5000)
print(user1.name)
print(user1.account_no)
# print(user1.balance)

print(user1.get_balance(123456))
# print(user1.get_balance(135791))

# =====================================================================
#                           4. Abstraction
# =====================================================================

# How to create abstract class?
# ABS --> Abstract Based Class

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def payment_process():
        pass
    
    @abstractmethod
    def refund():
        pass

# NOTE: We can not create an instance or obj from abstract class.

class Stripe(PaymentMethod): # normal class, not abstract class
    def payment_process(self):
        print('Stripe Payment Process')
    
    @abstractmethod
    def refund(self):
        print('Stripe Refund')

stripe = Stripe()



















