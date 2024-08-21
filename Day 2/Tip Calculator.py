print("Welcome to the tip calculator!")

bill = float(input("What is the total bill amount?\n$:"))
tip = float(input("How much tip would you like to give?\n$:"))
split = float(input("How many people to split the bill?\nPeople:"))

total = ((bill + tip)/ split)

print("Each person should pay: $", total)