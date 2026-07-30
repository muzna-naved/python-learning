dict = {
}

print(dir(dict))

# clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# clear --> Removes all items from the dictionary.
help(dict.clear)

student = {"name": "Muzna",
           "age": 20}
student.clear()
print(student)        

# copy --> Returns a shallow copy of the dictionary.
help(dict.copy)

student = {"name": "Muzna",
           "age": 20}
new_student = student.copy()
print(new_student)   

# fromkeys --> Creates a new dictionary with given keys and the same value for all keys.
help(dict.fromkeys)

keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)              

# get --> Returns the value of the given key. If the key is not found, returns the default value.
help(dict.get)

student = {"name": "Muzna"}
print(student.get("name"))       
print(student.get("age", 18))    

# items --> Returns all (key, value) pairs.
help(dict.items)

student = {"name": "Muzna",
           "age": 20}
print(student.items())

# keys --> Returns all the keys of the dictionary.
help(dict.keys)

student = {"name": "Muzna",
           "age": 20}
print(student.keys())

# pop --> Removes the specified key and returns its value.
help(dict.pop)

student = {"name": "Muzna",
           "age": 20}
age = student.pop("age")
print(age)            
print(student)        

# popitem --> Removes and returns the last inserted (key, value) pair.
help(dict.popitem)

student = {"name": "Muzna",
           "age": 20}
item = student.popitem()
print(item)           
print(student)        

# setdefault --> Returns the value of the key.
# If the key does not exist, it inserts the key with the given default value.
help(dict.setdefault)

student = {"name": "Muzna"}
student.setdefault("age", 20)
print(student)

# update --> Adds new key-value pairs or updates existing ones.
help(dict.update)

student = {"name": "Muzna", 
           "age": 20}
student.update({"age": 21, "city": "Karachi"})
print(student)

# values --> Returns all the values of the dictionary.
help(dict.values)

student = {"name": "Muzna", 
           "age": 20}
print(student.values())
