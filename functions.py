#function calling 
def sum(a,b): # parameters
    sum = a + b 
    print(sum)
    return sum

# fucntion calling 
sum(1,2) # arguments

# average of 3 numbers
def avg(a,b,c):
    sum = a + b + c 
    avg = sum/3
    print(avg)
    return avg

avg(3,2,1)

# built in fucntions
print("hello",end = " ") # print 
print("World")

# len() # type() # range()

#user defined fucntions

# default parameters
def product(a=3,b=2):
    print(a*b)
    return(a*b)

product() # a= 3 ,b=2

# print the length of a list 
def listLength(list):
    print(len(list))
    return(len)

cities = ["Karachi","Hyderabad","Lahore","Islamabad","Peshawar"]
listLength(cities)

# print the elements of a list in a single line
def printList(list):
    for el in list:
        print(el,end=" ")

cities = ["Karachi","Hyderabad","Lahore","Islamabad","Peshawar"]
printList(cities)

# factorial of n
def factorial(n):
    fact = 1
    for i in range(1,n+1):
       fact*=i
    print("\nfactorial of number is:",fact)
    
factorial(3)

# Convert USD in PKR
def USDToPkr(dollar):
    pkr = dollar * 278
    print("Dollars in pkr:",pkr," rupees")

USDToPkr(dollar = int(input("Enter amount in dolar: ")))
        
def converter(usd_val):
    pkr_val = 278*usd_val
    print(usd_val ,"USD = ",pkr_val,"pkr")

converter(100)
    
# input number and write even or odd
def evenOdd(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")

evenOdd(int(input("Enter number:")))
    