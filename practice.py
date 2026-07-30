# output 
print("Hello world!")
print(16)

name = "Muzna"
age =20 
isValid = True
price = None

print(name)
print(age)
print(isValid)
print(price)

print(type(name))
print(type(age))
print(type(isValid))
print(type(price))

# print sum
a=5
b=6
sum = a +b
print("SUm = " , sum)
print("Sum =" , a+b)
print("Sum = " , 5+7)

# Expression execution 

# if string and int are * together --> repetetion 
a,b=2,3
txt = "@"
print(a*txt*b)

# string and string can operate with + --> Append/Concatenation
a,b = "2",3
txt = "@"
print((a+txt)*b)

# numeric values can operate all arithmetic operators
a,b=2,3
c=4
print(a+b*c)

# arithmetic expression with integer and float will result in float 
a,b=10,5.0
c=a*b
print(c)

# result o division operator with two integers will be float 
a,b =1,2
c= a/b
print(c)

#integer division with float and int will give int displayed as float 
a,b=1.5,3
c=a//b
print(c,a/b) # if we divide normally it gives 0.5 but with integer division it gives 0.0

# floor gives closest integer,which is lesser than or equal to the float value
# result of a//b is same as floor(a/b)
a,b=12,5
c= a//b
print(c)

a,b=-12,5
c= a//b
print(c)

a,b=12,-5
c=a//b
print(c)

# reaminder is negative when denominator is negative 
a,b=-5,2
c=a%b
print(c)

a,b=5,2
c=a%b
print(c)

a,b=5,-2
c= a%b
print(c)

"""hello i am muzna
hello 
Hiii""" # multi line comment

# input 

# string 

name = input("Name: ")
print(name)

# int 
age = int(input("Age: "))
print(age)

# float 

price = float(input("Price: "))
print(price)
 
# exponent 

print(2**2)
print(2**3)

# conditional statements
#if elif else

# traffic lights

light = input("Color: ")
if (light == "Red"):
    print("stop")
elif(light ==  "Green"):
    print("go")
elif(light ==  "Yellow"):
    print("wait")
else:
    print("Light is broken")

# grading 

marks = int(input("Marks: "))
if(marks >= 90):
    print("A")
elif(marks>=80 and marks < 90 ):
    print("B")
elif(marks>=70 and marks < 80 ):
    print("C")
else:
    print("D")

#single line if / ternary operator

isPass = input("Pass or not :")
print("Pass") if isPass == "True" else print("Fail")

# clever if 
age = int(input("Age:"))
vote = ("yes","no") [age >=18]
print(vote)

sal = float(input("Salary : "))
tax = sal*(0.1,0.2) [sal <=50000]
print(tax)

# operators

#arithmetic 

a=4
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# relational
a= 50 
b=20

print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)
print(a<b)
print(a>b)
print(a==b)

# assignment 

a = 4
a+=1 
print(a)
a-=1 
print(a)
a*=1 
print(a)
a/=1
print(a)
a%=3
print(a)
a**=2
print(a)

#logical 

a=40
b=20

print(not True)
print(not (a>b))

a = True 
b = True
c = False

print(a and b )
print(a and c )

print(a or b)
print(a or c)

# type conversion
# conversion --> automatically 
#  casting --> manually --> convert one data tyoe in other 
a= int("2")
b=5
print(a+b)

# sum of two numbers
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
sum = num1 + num2
print("Sum is: ", sum)

# avg of two numbers
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
avg = (num1 + num2)/2
print("Avg is: ", avg)

# input two int numbers and check if a greater or equal than b if true write true else false 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if(a>=b):
    print("True")
else:
    print("False")
    
# strings
# length of string 
string = "MY Name is MUNZA"
print(len(string))

# concate 
str1= "Muzna"
str2 = "Naveed"
print(str1 + str2)
print( str1 + " " + str2)

# indexing 
# we only access characters but we cant change it by assigning
string = " MY NAME IS MUZNA"
print(string[3])

# slicing 
# accessing parts pf strings

string = "Muzna Naveed..."
print(string[1:3])
print(string[6:len(string)])
print(string[6: ]) # if we skip the second value it goes at the end of string auomatically
print(string[ :5 ]) # if we skip the first value it starts from idx 0 of string auomatically

# negatve indexing 

string = "Muzna Naveed..."
print(string[0:-3])

# string functions

string = "I am a coder"

# endswith -- > return true if strings end with substring 
print(string.endswith("er"))

# capatalize --> capatalized 1st character --> crreates new string ,does not change in original
str = "muzna"
print(str.capitalize())
print(str)
# if we want to change in original 
str = str.capitalize()
print(str)

# replace -->replaes all occurences of old

str = "Rumaisa-Muzna-Eshal"
print(str.replace("Muzna","Minnu"))

# find --> returns 1st index of 1s occurer
str = "Rumaisa-Muzna-Eshal"
print(str.find("M"))

# count--> counts occurences of substr
str = "Rumaisa-Muzna-Eshal"
print(str.count("a"))

# input user'first name and print its length

firstName = input("Enter your name:")
print("Lenght of name is :", len(firstName))

# find occurences of $ in a string 

str = "Apple = $20 ,Banana = $5 ,Orange = $40"
print("Occurences of $: ", str.count("$"))

# check if the entered number is even or odd

num = int(input("Enter a number: "))
if(num%2==0):
    print("Even")
else:
    print("Odd")
    
# find the greatest of 3 numbers entered by the user 
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
greatest = num1

if num2 > greatest:
    greatest = num2

if num3 > greatest:
    greatest = num3
print("Greatest number among 3 numbers is :",greatest)
    
# check if a number is multiple of 7 or not 
num = int(input("Enter number: "))
if(num% 7 ==0):
    print("NUMBER IS MULTIPLE OF 7 ")
else:
    print("NUMBER IS NOT MULTIPLE OF 7")

# Lists
# it can store elements of differnet types 
# strings -->immuntable -->not change 
#lists --> mutable -->change
marks = [45,50,55,30,20]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

student = [ "MUZNA ", 20, "KARACHI"]
print(student)
student[0] = "MINNU"
print(student)

# slicing --returns sublist
# same as string slicing 
list = [20,40,50,60]
print(list[0: 3])

# lists methods

# append --> adds one element at the end 
li = [1,2,3]
print(li.append(4))

# sort --> sorts in ascending order
li = [5,5,2,3,9]
print(li.sort())

#descending order
li = [5,5,2,3,9]
print(li.sort(reverse=True))

# reverse --> reverses the list 
li = [5,4,3,2,1]
print(li.reverse())

# insert -->insert element at index
li = [1,2,4,5,6]
print(li.insert(2,3))

# remove --> removes first occurence of element 
li = [1,1,2,3,4,5,7]
print(li.remove(1))

#pop --> removes element at index
li = [1,1,2,3,4,5,7]
print(li.pop(2))

# tuples
# tuples-->immutable

tuple = (1,2,3,4,5)
print(tuple[1])

# null tuple 
tup = ()
print(tup)
print(type(tup))

# single tuple 
tup = (1,)
print(tup)
print(type(tup))

#slicing 
tup = (1,2,3,4,5,6)
print(tup[1:3])

# slicing is same as stings and lists

# tuple methods

# index --> returns index of first occurrence 
tup = (1,2,3,4,5,6)
print(tup.index(1))

# count --> count total occurences 
tup = (1,2,3,4,5,5,6,1,2,3,6)
print(tup.count(1))

# ask the user enter names of their 3 favorites movies & store them in a list 
movie1 = input("Enter first movie:")
movie2 = input("Enter second  movie:")
movie3 = input("Enter third movie:")

list = [movie1,movie2,movie3]
print(list)

# another way 
movies= []

movie1 = input("Enter first movie:")
movie2 = input("Enter second  movie:")
movie3 = input("Enter third movie:")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

#another way 
movies= []

movies.append(input("Enter first movie:"))
movies.append(input("Enter second  movie:"))
movies.append(input("Enter third movie:"))

# check if a list contains palindrome of elements 
list = [1,2,1]
copiedList = list.copy()
copiedList.reverse()
if( list == copiedList):
    print("THE LIST IS PALINDROME ")
else:
    print("THE LIST IS NOT PALINDROME")

#dictionary 
# key:value pairs
# unordered,mutable,dont allow duplicate keys

info = {
    "name" : "Muzna",
    "age" : 20,
    "subjects" : ["Maths","Physics","Computer"],
    "topics" : ("Sets","Laws of motions","I/O")
}

print(info)
print(type(info))

print(info["name"])
print(info["subjects"])

info["name"] = "Minnu"
info["surname"] = "Naveed"
print(info)

# empty dict

null_dict ={}
print(null_dict)

null_dict["name"] = "RUMAISA"

# nested dictionaries

student = {
    "name" : "Muzna",
    "scores" : {
        "physics" : 99,
        "maths" : 89,
        "sst" : 70
    }
}
print(student)
print(student["scores"])
print(student["scores"]["maths"])

# dictionary methods

# keys --> return all keys
print(student.keys())

#values --> return all values
print(student.values())

# items --> returns all key value pairs as tuples
print(student.items())

# get --> returns the key according to value

# print(student["name1"]) # if name1 does not exist it gives error
print(student.get("name1")) # if name1 does not exist it gives none

# update --> inserts the specified items to the dictionary 

student.update({"city" : "KARACHI" , "age" : 20})
print(student)

#sets
# collection of unorederd items
# sets --> mutable 
# each element must be unique and immutable

collection = {1,2,34,5}
print(collection)
print(type(collection))
print(len(collection))

# empty set 

collection = set()

print(type(collection))

# set methods

# add --> adds an element 
collection.add("MUZNA")
collection.add("Eshal")
collection.add("FABHA")

print(collection)

# remove -->remove the element
collection.remove("MUZNA")
print(collection)

# pop--> removes a random value
collection.pop()
print(collection)

# clear -->empties the set
collection.clear()
print(collection)

# union --> combines both set values & returns new 

set1 = {1,2,4,5,2,4}
set2 ={8,57,9,4,2,4,6}

print(set1.union(set2))

#intersection --> combines common values and returns new


set1 = {1,2,4,5,5,2,2,6,2,4}
set2 ={8,57,9,2,2,2,25,6,5,6,4,2,4,6}

print(set1.intersection(set2))

# store following words meanings in a python dictionary 

dict = {
    "table" : ["a piece of furniture", "lists of facts and figures"],
    "cat" : "a small animal"
}

print(dict)

# you are given a subject list of subjects for students .Assume one classroomis required for 1 subject .How many classrooms are needed by all students 
set = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(set)
print("Total classrooms : ", len(set))

# enter marks of 3 subjects from the user and store them in a dictionary.STart with an emoty dictionary & add one by one .Use subject as key & marks as values

marks1 = int(input("ENter maths marks: "))
marks2 = int(input("ENter Urdu marks: "))
marks3 = int(input("ENter COmputer marks: "))

dict = {}

dict.update({"maths" : marks1})
dict.update({"Urdu " : marks2})
dict.update({"Computer" : marks3})

print(dict)

# Fgure out a way to store 9 & 9.0 as separate values in the set.(you cantake help of built-in data types)

# first solution 
values = {9,"9.0"}
print(values)

# second solution 
values = {
    ("float", 9.0),
    ("int",9)
}

# loops 

# while loop
i=1
while i <=6:
    print(i)
    i+=1

# print number from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
    
# print number from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
    
# print a multiplication table of number n 
num = int(input("Enter number:"))
i=1 
while i<=10:
    print(num ,"x" ,i ,"=" ,num*i)
    i+=1
    
# print the elements of the following lists using loop
li = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i<= len(li)-1:
    print(li[i])
    i+=1
    
# search for a number x in this tuple using loop 
tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter number:"))
i=0
while i<=len(tup)-1:
    if(tup[i]==x):
        print("Number found at: ", i)
    i+=1

# break 
i=1
while i<=5:
    print(i)
    if(i == 3):
        break
    i+=1
    
# continue 
i=1
while i<=5:
    if(i == 3):
        i+=1
        continue
    print(i)
    i+=1

# for loop 

list = [1,2,3,4,5]
for el in list:
    print(el)

tup = (1,2,3,4)
for el in tup:
    print(el)

string = "Muzna Naveed"
for char in string:
    print(char)
else:
    print("END") 

# search for a number x in this tuple using loop
tup = (1,23,4,5,67,8,7,6,5,10)
x= int(input("Enter number:"))
idx=0
for el in tup:
    if(el==x):
        print("Number found at:",idx)
        idx+=1
        break
    else:
        print("Number not found") 
          
# range 
for el in range(10): # range (stop)
    print(el)
    
for el in range (1,10): #eange(start?,stop)
    print(el)
    
for el in range(1,10,2): #range(start?,stop,step)
    print(el)
    
# print number from 1 to 100
for el in range (1,101):
    print(el)

# print number from 100 to 1
for el in range (100,0,-1):
    print(el)

# print multiplication table of number n 
num = int(input("Enter number:"))
for i in range(1,11):
    print(num,"x" ,i,"=",num*i)
    
# pass statement -->Null .Its a placeholder for future code 
for i in range(5):
    pass

if i>5:
    pass

# sum  of first n numbers (using while)
i=1
sum =0
n = int(input("Enter number:"))
while i<=n:
    sum+=i
    i+=1
    
print("Sum of n numbers is:",sum)

# factorial of first n numbers using for 
n = int(input("Enter number:"))
fact =1
for i in range(1,n+1,1):
    fact=fact*i
    
print("Factorial of number is : ",fact)
    