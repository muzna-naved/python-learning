height = float(input("Enter height of the cube:"))
width = float(input("Enter width of the cube:"))
depth = float(input("Enter depth of the cube:"))
volume = height*width*depth
print("The volume of the cube is: ",volume)
if(volume>=251):
    print("Extra extra large")
elif(volume >=101 and volume<=250):
    print("Extra large")
elif(volume >= 76 and volume <= 100):
    print("Large")
elif(volume >= 26 and volume <= 75):
    print("Medium")
elif(volume >= 11 and volume <= 25):
    print("Small")
elif(volume >=1 and volume <= 10):
    print("Extra small")
else:
    print("Volume out of range!")