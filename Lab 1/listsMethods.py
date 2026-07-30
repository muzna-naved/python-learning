#'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',  'sort

list = ["apple","Mango","banana","orange","grapes","apple"]

print(dir(list))

# append --> append at the end of the list
help(list.append)
list.append("cherry")
print(list)

# count --> return number of occurences
help(list.count)
print(list.count("apple"))

# extend --> adds multiple items
help(list.extend)
list.extend(["peach","strawberry"])
print(list)

# index --> returns first index of value
help(list.index)
print(list.index("Mango"))

# insert--> insert object before index
help(list.insert)
list.insert(1,"kiwi")
print(list)

# pop -->  Remove and return item at last index
help(list.pop)
print(list.pop())
print(list)

# remove --> Remove first occurrence of value.
help(list.remove)
list.remove("apple")
print(list)

# reverse -->  Reverse IN PLACE.
help(list.reverse)
li = [1,2,3,4,5]
li.reverse()
print(li)

# sort -->  Sort the list in ascending order and return None.
help(list.sort)
list1 = [5,7,8,9,3,5,1,0,1,3]
list1.sort()
print(list1)