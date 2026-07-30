#  list comprehension which, from a list, generates a lowercased version of each string that has 
# length greater than five. 
strings = ["HELLO","MUZNA","BYE","PANDA","ORANGE","PAPAYA","MONKEY","KARACHI"]
lowercase= [s.lower() for s in strings if len(s)>5]
print(lowercase)

# program to print a specified list after removing the 0th, 4th and 5th elements  
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’] 
# Expected Output : ['Green', 'White', 'Black'] 

li = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink']

new_list = [li[i] for i in range(len(li))  if i not in (0,4,5)]
print(new_list)
