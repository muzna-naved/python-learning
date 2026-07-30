#  program to convert temperatures to and from celsius,Fahrenheit. 

print("Temperature conversions".center(40, "-"))
print("1.Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = int(input("Enter your choice (1 or 2): "))

if(choice == 1):
    fahrenheitTemp = float(input("Enter temperature in Fahrenheit: "))
    c = (fahrenheitTemp - 32) * 5 / 9
    print("Temperature in Celsius is: ",c)
elif(choice == 2):
    celsiusTemp = float(input("Enter temperatire in Celsius: "))
    f = (celsiusTemp * 9 / 5) + 32
    print("Temperature in Fahrenheit is: ",f)
else:
    print("Invalid choice!!")
    

    

 

