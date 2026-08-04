# loops and recursion are interrelated
#  prints n to 1 backwards
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(10)

# factorial 
def factorial(n):
    if(n==0 or n==1):
        return 1 
    else: 
        return n* factorial(n-1)
    
print(factorial(4))

# calculate the sum of first n natural numbers

def sumOfNNumbers(n):
    if(n==0):
        return 0
    return sumOfNNumbers(n-1) + n

print(sumOfNNumbers(3))

# print all elements in a list 
def printList(list,index=0):
    if(index == len(list)):
        return
    print(list[index]) 
    printList(list,index + 1)

list = ["Zunair","Khuzaima","Arsal","Aliyan"]
printList(list)