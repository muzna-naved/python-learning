username = input("Enter username:")
password = input("Enter password:")

knownPassword = "abc$123"
password = password.lower()
if(password == knownPassword):
    print("Welcome!")
else:
    print("I don't know you.")
   