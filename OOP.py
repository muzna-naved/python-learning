# class --> blueprint 
# class have attributes and methods 
class Student:
    name = "Muzna"

# object --> instance

s1 = Student() # first object
print(Student.name)

s2 = Student() # second object
print(Student.name)

class Car:
    color = "Black" # class attribute 
    brand = "Mercedes"

c1 = Car()
print(Car.color)
print(Car.brand)

# _init_ sunction (constructor) --> All classes have a function called init(),which is always executed when the object is being initiated
# the self parameter is a refernece to the current instance of the class , and is used to access variablesthat belong to the class 
# attrbutes --> data,variables

class Shape:
    # self constructor
    # def __init__(self):
    #     pass
    # parameterized constructor
    def __init__(self,name,color):
        self.name = name
        self.color = color # instance attribute
        print("adding new shape in databae..")
        
    @staticmethod # decorator
    def hello():
        print("Hello..")
        
# decorators allow us to wrap another function in order to extend the behavior of the wrapped function,without permanently modyfing it 

shape1 = Shape("Circle","Blue")
print(shape1.name)
print(shape1.color)
shape1.hello()
        
shape2 = Shape("Triangle","Yellow")
print(shape2.name)
print(shape1.color)

# class attribute --> common --> same for all
# instance attribute --> different for all (self.name=name)
# obj attribute > class attribute (preceendence is higher of obj attribute)

# methods are objects that belongs to objetcs

# create student class that takes name and marks of 3 subjects as arguments in constructor .Then create a method to print the average 

class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
        
    def avgOfMarks(self):
        sum = 0 
        for val in self.marks:
            sum+=val
        print(self.name,"'s ","Average of marks is : ",sum/3)

s1 = Student("Muzna",[99,89,70])
s1.avgOfMarks()
s2 = Student("Eshal",[80,90,70])
s2.avgOfMarks()

# static method --> dont use self parameters (work at class level)

# pillars of OOP 
# abstraction --> hiding the implementation details of a class and only showing the essential features to the user 
# encapsulation --> Wrapping data and fucntions into a single unit (object)
# polymorphism -->
# inheritance --> 

# abstraction 

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started ..")

car1 = Car()
car1.start()

# encapsulation

class Patient:
    def __init__(self,name,disease,age):
        self.name = name
        self.disease = disease
        self.age = age

p1 = Patient("Rumaisa","Fever",23)
print(p1.name,p1.disease,p1.age)

# create Account class with 2 attributes - balance and account no.Create method for debit,credit & printing the balance 
class Account:
    def __init__(self,balance,accNo):
        self.balance = balance
        self.accNo = accNo
    
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount ,"was debited")
        print("total balance: ",self.printBalance())
    
    def credit(self,amount):
            self.balance += amount
            print("Rs.",amount ,"was credited")
            print("total balance: ",self.printBalance())

    def printBalance(self):
        return self.balance        
        
acc1 = Account(1000000,2887899)
acc1.debit(2000)
acc1.credit(30000)
print(acc1.balance)

# del keyword --> used to delete object properties or object itself 

class Student:
    def __init__(self,name):
        self.name = name 

s1 = Student("Eshal")
print(s1.name)
del s1.name

# priavte attributes & methods --> private attributes and methods are meant to be used only within the class and are not acccessible from outside the class 

# class Account:
#     def __init__(self,accNo,accPass):
#         self.accNo = accNo
#         self.__accPass = accPass
    
#     def resetPassword(self):
#         print(self.__accPass)
    

# acc1 = Account("235678","2006")
# print(acc1.accNo)
# print(acc1.accPass)
# print(acc1.resetPassword())

# class Person:
#     __name = "anonymous"
    
#     def __hello():
#         print("Hello person!")
    
#     def welcome(self):
#         self.__hello()
    
# p1 = Person()
# print(p1.welcome())

# inheritance --> when one class (child/derived) derives the properties & methods of another class(parent/base)
# single inheritance --> one parent --> one child
class Car:
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..")
    color = "black"

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

c1= ToyotaCar("fortuner")
c2= ToyotaCar("prius")

print(c1.start())
print(c1.color)

# Multi-level inheritance --> multiple parent --> multiple child
class Car:
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..")
    color = "black"

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        
c1= Fortuner("diesel")
c1.start()

# Multiple inheritance --> multiple parent --> single child 
class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class C"
    
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

# super() method is used to access methods of the parent class 
class Car:
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..")
    color = "black"

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

c1= ToyotaCar("fortuner","electric")
print(c1.type)

# class method is bound to the class & receives the classas an implicit first argument
# static method cant access or modify class state class state & generally for utility 

class Person:
    name = "anonymous "
     
    def changeName(self,name):
        self.name = name 

p1= Person()
p1.changeName("Muzna")
print(p1.name)
print(Person.name)  # it does not give name Muzna it gives anonymous .It does not change class attribute directly

# first way
class Person:
    name = "anonymous "
     
    def changeName(self,name):
        Person.name = name   # we use class name . attribute and now it gives same name as object

p1= Person()
p1.changeName("Muzna")
print(p1.name)
print(Person.name) 

# second way 
class Person:
    name = "anonymous "
     
    def changeName(self,name):
        self.__class__.name = name   # we use __class__ and now it gives same name as object

p1= Person()
p1.changeName("Muzna")
print(p1.name)
print(Person.name) 

# class method decorator 
class Person:
    name = "anonymous "
     
    @classmethod
    def changeName(cls,name):
       cls.name = name

p1= Person()
p1.changeName("Muzna")
print(p1.name)
print(Person.name) 

# static method --> no arguments
# class method --> first argument --> cls
#  instance method --> first argument --> self

# property decorator --> we use property decorator on any method in the class to use the method as a property 
class Student:
    def __init__(self,phy,math,chem):
        self.phy = phy
        self.math= math
        self.chem = chem
    
    @property
    def percentage(self):
        return str((self.phy+self.math+ self.chem)/3) + "%"
        
stu1 = Student(89,98,97)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)

# polymorphism --> --> many forms --> opeartor overloading
# when the same operator is allowed to have different meaning according to the context 
 
# dunder functions --> double underscroe 

class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def showNumber(self):
        print(self.real,"i + ",self.imaginary,"j")
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImagianry = self.imaginary + num2.imaginary
        return Complex(newReal,newImagianry)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImagianry = self.imaginary - num2.imaginary
        return Complex(newReal,newImagianry)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()

# define a circle class to create a circle with radius r using the constrcutor.Define an area() method of the class which calculate the area of the circle .Define a perimeter() method of the class allows you to calculate the perimeter of the circle 

class Circle:
    def __init__(self,r):
        self.r = r
        
    def area(self):
        area = (3.142)*self.r**2
        print("Area of circle is: ",area)
    
    def perimeter(self):
        perimeter = 2*3.142*self.r
        print("The perimeter of circle is:",perimeter)

c1 = Circle(21)  
c1.area()
c1.perimeter()

# Define a Employee class with attributes role,department, & salary. this class also has a showDetails() method .Creates am Engineer class that inherits properties from Employee & has additional attributes: name & age   
class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self):
        print("Role:",self.role,"\nDepartment:",self.department,"Salary:",self.salary)

class Engineer(Employee):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","750000")
        super().showDetails()
        print("Name:",self.name)
        print("Age:",self.age)

e1 = Employee("Accountant","Finance","600000")
e1.showDetails()

eng1 = Engineer("Muzna","20")
eng1.showDetails()

# Create a class Order which stores item & its price .Use dunder fucntion __gt__() to convey that order1 > order2 if price of order 1 > price of order2 
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def _gt__(self,order2):
        return self.price > order2.price

ord1 = Order("Lays","100")
ord2 = Order("Biscuit","50")

print(ord1>ord2)
         

        
    






        


