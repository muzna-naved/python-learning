import random
import string

pass_len = int(input("Enter password length:"))

charValues = string.ascii_letters + string.digits + string.punctuation
print(charValues)

# using list comprehension
password = "".join([random.choice(charValues) for i in range(pass_len)])
print("Your random password is:",password)

# using for loop
password =""
for i in range(pass_len):
    password += random.choice(charValues)
print("Your random password is:",password)

