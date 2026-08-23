# You have collected information about cities in your province. You decide to store each city’s 
# name, population, and mayor in a file. Write a python program to accept the data for a number of 
# cities from the keyboard and store the data in a file in the order in which they’re entered.

number = int(input("Enter the number of cities: "))

with open("cities.txt", "w") as f:
    for i in range(number):
        print("\nEnter information for city", i + 1)

        name = input("Enter city name: ")
        population = input("Enter population: ")
        mayor = input("Enter mayor name: ")

        f.write("City: " + name + "\n")
        f.write("Population: " + population + "\n")
        f.write("Mayor: " + mayor + "\n")

