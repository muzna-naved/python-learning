# program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
list = []
list.append(input("Enter string 1: "))
list.append(input("Enter string 2: "))
list.append(input("Enter string 3: "))
list.append(input("Enter string 4: "))
list.append(input("Enter string 5: "))
list.append(input("Enter string 6: "))

print(list)
count =0
for el in list:
    if(len(el)>=2 and (el[0] == el[-1])):
        count+=1
print(count)
