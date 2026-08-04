# Python can be used to perform operations on a file (read and write data)
# Types pf files 
# text files : .txt, .docx, .log etc
# binary files: .mp4 , .mov , .png , .jpeg etc

# raeding 
f = open(r"C:\Users\pc\Downloads\DSA.txt","r")
data = f.read()
print(data)
print(type(data))
fiveCharcters = f.read(5)
print(fiveCharcters)
firstLine = f.readline()
print(firstLine)
secondLine = f.readline()
print(secondLine)
f.close()

# writing 
# w --> overwite 
# a --> append --> add at the end 

f = open(r"C:\Users\pc\Downloads\DSA.txt","a")
f.write("Hello,I am Muzna")
f.close()

# if we open a file in w or a mode and the file does not exists,python automatically create the file 
# w+ --> read and overwrite,write and writing from the starting , reading data form where the pointer stops ,no truncate 
# r+ --> read and overwrite, truncates the file --> completely wiped out 
# a+ --> read and append , append from end ,no truncate 

# with syntax
# with automatically close file 

#read 
with open(r"C:\Users\pc\Downloads\DSA.txt","r") as f:
    data = f.read()
    print(data)
    
# write
with open(r"C:\Users\pc\Downloads\DSA.txt","a") as f :
    f.write("Hiii")
    
# deleting a file 
# using the os module 
# Module (like a code library) is a  file written by another programmer that generally has a functins we can use 

# import os

# os.remove("sample.txt") 

# create a new file "practice.txt" using python .Add following data in it

with open("practice.txt","w") as f :
    f.write("Hi everyone\nwe are learning file I/O \nusing java.\nI like programming in java.")
    
# replace all occurences of java with python 
with open("practice.txt","r") as f :
    data = f.read()
    newData = data.replace("java","pyhton")
    print(newData)
    
with open("practice.txt","w") as f :
    f.write(newData)
    
# search if the word learning exists in the file or not 
with open("practice.txt","r") as f :
    word = "learning"
    data = f.read()
    if(word in data):
        print("Yes it exists")
    else:
        print("No,it deos not exist")
    
# find in which line of the file does the word learning occur first.pritn -1 if word not found 
def checkForLine():
    word = "learning"
    data = True
    lineNumber = 1
    with open("practice.txt","r") as f :
        while data:
            data = f.readline()
            if(word in data ) :
                print("It is in line number: ", lineNumber)
                return
            lineNumber +=1
        return -1

print(checkForLine())

# from a file containing numbers separated by comma,print the count of even numbers

with open("numbers.txt","r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")
    print(nums)
    count =0 
    for el in nums:
        if(int(el) % 2 == 0):
            print(el)
            count+=1
print(count)
        