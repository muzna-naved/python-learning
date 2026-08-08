import random

target = random.randint(1,100)

while True:
    userChoice = int(input("Guess the target or Quit:"))
    if(userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small..take a bigger guess..")
    else:
        print("Your number was too big..take a smaller guess..")
print("GAME OVER!!")