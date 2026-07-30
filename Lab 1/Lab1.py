# python prompt >>>
# It appears only in interactive mode.

# Boolean operators 
1==0  
not (1==0)    
(2==2) and (2==3)   
(2==2) or (2==3)    

# Strings 

# concatenation
print('artificial' + "intelligence")
# upper
print("artificial".upper())
# lower 
print("artificial".lower())
# length 
print(len("help"))

# We can also store expressions into variables. 
s = 'hello world'
print(s) 
print(s.upper())   
print(len(s.upper()))   
num = 8.0    
num += 2.5    
print(num)   
#  you do not have declare variables before you assign to them.   

# lists 
# Lists store a sequence of mutable (changeable) items
fruits = ['apple','orange','pear','banana'] 
print(fruits[0])

#  concatenation
otherFruits = ['kiwi','strawberry']   
print( fruits + otherFruits)

# list allows negative-indexing from the back of the list. 
print(fruits[-1])
# pop -->removes last element 
fruits.pop()
print(fruits)

# append --> add element at the end 
fruits.append('grapefruit') 
print(fruits)
# update 
fruits[-1] = 'pineapple'
print(fruits)
   
# slice -->  index multiple adjacent elements 
# [start:stop]
print(fruits[0:2])
# [ : stop ] start 0 by default
print(fruits[ : 3])
# [0 :  ] end last index by default 
print(fruits[0: ])

# list of list 
lstOfLsts = [['a','b','c'],[1,2,3],['one','two','three']]  
print(lstOfLsts[1][2])
lstOfLsts[0].pop()
print(lstOfLsts)
print(lstOfLsts[0][1])
lstOfLsts[0].pop()
print(lstOfLsts)
lstOfLsts[0].pop()
print(lstOfLsts)

#  tuples --> data structure similar to the list is the tuple, which is like a list except that it is immutable once it is 
# created 
pair = (3,5)
print( pair[0] )
x,y = pair
print(x)
print(y)
# pair[1] = 6   TypeError: object does not support item assignment  

# Sets --> A set is another data structure that serves as an unordered list with no duplicate items.
# first way 
shapes = ['circle','square','triangle','circle']
setOfShapes = set(shapes)   
# another way 
setOfShapes = {'circle', 'square', 'triangle', 'circle'}  

setOfShapes.add('polygon')    
print(setOfShapes)

print('circle' in setOfShapes )   
print('rhombus' in setOfShapes)   
 
favoriteShapes = ['circle','triangle','hexagon'] 
setOfFavoriteShapes = set(favoriteShapes)

# operations (difference, intersection, union): 

print(setOfShapes - setOfFavoriteShapes)  # difference 
print(setOfShapes & setOfFavoriteShapes)   #intersection 
print(setOfShapes | setOfFavoriteShapes) # Union   

# Dictionaries   --> key value pair 
# The key must be an immutable type (string, number, or tuple). The value can be any 
# Python data type.   

studentIds = {'knuth': 42.0,
              'turing': 56.0, 
              'nash': 92.0 }

print(studentIds['turing'] )

studentIds['nash'] = 'ninety-two'   
print(studentIds)   

del studentIds['knuth']   
print(studentIds)   

studentIds['knuth'] = [42.0,'forty-two']   
print(studentIds)   
print(studentIds.keys())   
print(studentIds.values())  
print(studentIds.items() )
print( len(studentIds) )
#  you can also create dictionaries of dictionaries.  

# writing scripts 
fruits = ['apples', 'oranges', 'pears', 'bananas']  #lists
for fruit in fruits:   # for each loop  
    print(fruit + ' for sale')   
fruitPrices = {'apples': 2.00,
               'oranges': 1.50,
               'pears': 1.75} # dictionary 
for fruit, price in fruitPrices.items():   # for each loop   
    if price < 2.00:          
        print('%s cost %f a pound' % (fruit, price))     
        print(fruit + ' are too expensive!')  
        
# map --> applies this function to every element in the list.
print(list(map(lambda x: x * x, [1,2,3])) ) # lambda x: x * x small anonymous function

# filter --> keeps only the elements that satisfy the condition.
print( list(filter(lambda x: x > 3, [1,2,3,4,5,4,3,2,1])))

# list comprehension --> Creates a list in one line
# Instead of writing

# plusOneNums = []

# for x in nums:
#     plusOneNums.append(x + 1)

nums = [1,2,3,4,5,6] 
plusOneNums = [x + 1 for x in nums]
print(plusOneNums)
oddNums = [x for x in nums if x % 2 == 1] 
print(oddNums)   
oddNumsPlusOne = [x+1 for x in nums if x % 2 ==1]
print(oddNumsPlusOne)  
  
# Dir and Help   
str = "hello world"
# The dir() function lists all the attributes and methods of an object.
print(dir(str))

# The help() function explains what a function or method does and how to use it.
help(str.upper)
help(str.replace)

# converts to upper case 
name = "python"
print(name.upper())
# converts to lower case
name = "PYTHON"
print(name.lower())
# replace text
text = "I like Python"
print(text.replace("Python", "Java"))
# split strings into words
sentence = "Apple Mango Banana"
print(sentence.split())
# find --> Find a word
text = "Hello World"
print(text.find("World"))

#  'capitalize', 'center', 'count', 'decode', 
# 'encode', 'endswith',   
# 'expandtabs', 'find', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower',   
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',   
# 'replace', 'rfind','rindex', 'rjust', 'rsplit', 'rstrip', 'split',   
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',  'upper', 'zfill'

# capatalize 
print(str.capitalize())
# center align
print("abc".center(5))
name = "Ali"
print(name.center(10))
print("abc".center(10, "*"))
# count 
print("Hello world".count("o"))
# ends with --> it returns true if string ends matches 
print(str.endswith("ld"))
# expand tabs 
print(str.expandtabs())
# find --> finds first occurence. If the value is not found, it returns -1.
text = "Hello"
print(text.find("el"))
# index --> If the value is not found, it gives an error.
print("Hello".index("e"))
# isalnum --> returns true if it has alphabet and numerics
print("muzna2006".isalnum())
# isalpha --> returns true if it has alphabets only 
print("feb".isalpha())
# isdigit --> returns true if it has only digit 
print("123".isdigit())
# islower --> Return True if the string is a lowercase string
print("str".islower())
# isspace --> Return True if the string is a whitespace string
print(" ".isspace())
# istitle --> each word starts with a capital letter).
print("Muzna Naveed".istitle())
# isupper --> return trrue if the string is a uppercase string
print("MUZNA".isupper())
# join --> joins elements of a list (or other iterable) into one string.
words = ["Hello", "World"]
print(" ".join(words))

items = ["apple", "banana", "mango"]
print("-".join(items))

letters = ["P", "y", "t", "h", "o", "n"]
print("".join(letters))

numbers = ["1", "2", "3"]
print(",".join(numbers))
# ljust --> left justify.
print("Hi".ljust(10, "-"))
# rjust--> right justify 
print("Hi".rjust(10, "-"))
# lower--> Return a copy of the string converted to lowercase.
print(str.lower())
# lstrip --> removes characters from the left side (beginning) of a string.
text = "   Hello"
print(text.lstrip())

text = "###Python"
print(text.lstrip("#"))

text = "abcabcHello"
print(text.lstrip("abc"))

# replace --> replace one part of a string with another part.

text = "I like Python"
print(text.replace("Python", "Java"))

text = "apple apple apple"
print(text.replace("apple", "mango"))

text = "apple apple apple"
print(text.replace("apple", "mango", 2))

text = "banana"
print(text.replace("a", "o"))

# rfind --> finds the last occurrence (rightmost position) of a substring in a string.
text = "banana"
print(text.rfind("a"))

text = "hello world"
print(text.rfind("o"))

text = "Python"
print(text.rfind("z"))

# rindex --> finds the last occurrence (rightmost position) of a substring in a string.
text = "banana"
print(text.rindex("a"))

text = "hello world"
print(text.rindex("o"))

# rsplit --> splits a string into a list of parts, starting the split from the right side.
text = "apple mango banana" # By default, it splits on spaces.
print(text.rsplit())

text = "apple,mango,banana" # The comma is used as the separator.
print(text.rsplit(","))

text = "one-two-three-four"
print(text.rsplit("-", 2))

# rstrip--> removes characters from the right side (end) of a string.
text = "Hello     "
print(text.rstrip())

text = "Hello!!!"
print(text.rstrip("!"))

text = "Pythonabc"
print(text.rstrip("abc"))

# split --> breaks a string into a list of smaller strings.
text = "Hello Python World"
print(text.split())

text = "apple,mango,banana"
print(text.split(","))

text = "one-two-three-four"
print(text.split("-", 2))

sentence = "I love programming"
words = sentence.split()
print(words)

# splitlines --> splits a string into a list of lines.It separates the string wherever it finds a line break (\n, \r\n, etc.).

text = "Hello\nPython\nWorld"
print(text.splitlines())

message = """My name is Ali
I am learning Python
Python is easy"""
print(message.splitlines())

text = "Hello\nPython\nWorld"
print(text.splitlines(True))

# startswith --> return true if string starts with this
print("Helloooo".startswith("He"))

# strip --> removes characters from both sides (left and right) of a string.
text = "   Hello Python   "
print(text.strip())

text = "###Python###"
print(text.strip("#"))

text = "abcPythonabc"
print(text.strip("abc"))

# swapcase --> changes the case of every letter: Uppercase letters → become lowercase Lowercase letters → become uppercase
text = "Hello Python"
print(text.swapcase())

text = "python"
print(text.swapcase())

# title --> converts a string into title case.
text = "hello python"
print(text.title())

# translate --> replaces characters in a string using a translation table.
text = "hello"
table = str.maketrans("h", "H")
print(text.translate(table))

text = "hello world"
table = str.maketrans("hw", "HW")
print(text.translate(table))

text = "hello123"
table = str.maketrans("", "", "123")
print(text.translate(table))

text = "Hello, World!"
table = str.maketrans("", "", ",!")
print(text.translate(table))

# upper --> converts all lowercase letters in a string into uppercase letters.
text = "hello python"
print(text.upper())

# zfill --> adds zeros (0) at the beginning of a string until the string reaches a specified length.The "z" means zero fill.
num = "25"
print(num.zfill(5))

text = "123"
print(text.zfill(6))

text = "Hello"
print(text.zfill(3))

num = "-45"
print(num.zfill(5))

student_id = "7"
print(student_id.zfill(4))

# operators
# Arithmetic Operators

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Assignment Operators

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 2
print(x)

# Comparison Operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical Operators

a = True
b = False

print(a and b)
print(a or b)
print(not a)

# Bitwise Operators

a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)

# Membership Operators

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("orange" in fruits)
print("orange" not in fruits)








