timeTaken = float(input("Enter the time taken by the worker:"))
print("The time taken by the wroker is: ",timeTaken," hours")
if(timeTaken > 5):
    print("You need to leave the company")
elif(timeTaken > 4 and timeTaken <= 5):
    print("You will be given training to improve your speed")
elif(timeTaken > 3 and timeTaken <= 4):
    print("improve your speed.")
elif(timeTaken >= 2 and timeTaken <=3):
    print("highly efficient.")
else:
    print("Time entered is out of the expected range")
    