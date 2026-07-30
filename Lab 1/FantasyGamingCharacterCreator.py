# ===================================================================
# FANTASY CHARACTER CREATOR
# ===================================================================

# TASK 1: INTRODUCTION
# -------------------------------------------------------------------
# This program creates a fantasy character. The user picks a class,
# a weapon, and three items. At the end it shows a full summary.

# TASK 2: TERMINAL
# -------------------------------------------------------------------
# Run this program in the terminal using:
#     python fantasy_character_creator.py

# TASK 3: PYTHON INTERPRETER
# -------------------------------------------------------------------
# The interpreter reads this file line by line and runs it.

print("=====================================")
print("Fantasy Character Creator")
print("=====================================")
print("Welcome Hero!")

# TASK 7: LISTS AND TUPLES
# tuple, fixed list of classes
classes = ("1.Wizard", "2.Knight", "3.Archer")

# TASK 10: USER INPUT AND THE WHILE LOOP
while True:
    # TASK 4: VARIABLES
    name = input("Enter your name: ")

    # TASK 9: THE FOR LOOP
    for el in classes:
        print(el)

    classChoiceInput = input("Enter your choice: ")

    # TASK 8: CONDITIONAL STATEMENTS
    if classChoiceInput.isdigit() == False:
        print("Invalid choice")
        continue

    classChoice = int(classChoiceInput)

    if classChoice == 1:
        className = "Wizard"
        health = 80
        attack = 120
    elif classChoice == 2:
        className = "Knight"
        health = 150
        attack = 90
    elif classChoice == 3:
        className = "Archer"
        health = 100
        attack = 110
    else:
        print("Invalid choice")
        continue

    print("Available weapons: ")
    print("Sword\nBow\nMagic Staff")
    weaponChoice = input("Choose weapon: ").title()

    # TASK 5: OPERATORS
    if weaponChoice == "Sword":
        attack += 20
    elif weaponChoice == "Bow":
        attack += 15
    elif weaponChoice == "Magic Staff":
        attack += 30
    else:
        print("Invalid weapon! No bonus added.")

    # TASK 7: LISTS AND TUPLES
    inventory = []   # list
    print("Choose three items: ")
    print("Potion\nShield\nMap\nFood\nTorch\nArrow")
    inventory.append(input("Enter item 1: "))
    inventory.append(input("Enter item 2: "))
    inventory.append(input("Enter item 3: "))

    # TASK 6: DICTIONARY
    character = {
        "Name": name,
        "Class": className,
        "Health": health,
        "Attack": attack,
        "Weapon": weaponChoice,
        "Inventory": inventory
    }

    print("\nCharacter Summary")
    for key, value in character.items():
        print(key, ":", value)

    print("\nInventory:")
    for item in inventory:
        print("-", item)

    choice = input("Create another character? (Y/N):")
    if choice.upper() == "N":
        break

print("\nThank you for using Fantasy Character Creator!")