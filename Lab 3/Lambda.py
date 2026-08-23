# program to square and cube every number in a given list of integers using Lambda.  

# numbers = [1, 2, 3, 4]

# square = lambda a: a ** 2
# cube = lambda a: a ** 3

# squares = list(map(square, numbers))
# cubes = list(map(cube, numbers))

# print("Squares:", squares)
# print("Cubes:", cubes)

# program to find if a given string starts with a given character using Lambda.  
# s= "Muzna here"
# ch = 'M'
# x = lambda s : s[0] == ch
# print(x(s))

# program to extract year, month, date and time using Lambda

from datetime import datetime

now = datetime.now()

year = lambda x: x.year
month = lambda x: x.month
date = lambda x: x.day
time = lambda x: x.time()

print("Year:", year(now))
print("Month:", month(now))
print("Date:", date(now))
print("Time:", time(now))