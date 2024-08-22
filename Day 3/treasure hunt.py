# Treasure Hunt Game

print("Welcome to the Treasure Hunt Game!")
print("Answer the following questions to find the treasure.")
print("If you answer incorrectly, the game is over.\n")

# Question 1
answer = input("1. What is the capital of France? ").lower()
if answer == "paris":
    print("Correct! You move on to the next question.\n")
else:
    print("Wrong answer. Game over!")
    exit()

# Question 2
answer = input("2. What is 5 + 7? ")
if answer == "12":
    print("Correct! You move on to the next question.\n")
else:
    print("Wrong answer. Game over!")
    exit()

# Question 3
answer = input("3. Which planet is known as the Red Planet? ").lower()
if answer == "mars":
    print("Correct! You move on to the next question.\n")
else:
    print("Wrong answer. Game over!")
    exit()

# Question 4
answer = input("4. What is the square root of 64? ")
if answer == "8":
    print("Correct! You move on to the next question.\n")
else:
    print("Wrong answer. Game over!")
    exit()

# Question 5
answer = input("5. Who wrote 'Romeo and Juliet'? ").lower()
if answer == "william shakespeare" or answer == "shakespeare":
    print("Correct! You move on to the next question.\n")
else:
    print("Wrong answer. Game over!")
    exit()

# Question 6
answer = input("6. What is the largest ocean on Earth? ").lower()
if answer == "pacific ocean" or answer == "pacific":
    print("Correct! You move on to the next question.\n")
else:
    print("Wrong answer. Game over!")
    exit()

# Question 7
answer = input("7. How many continents are there on Earth? ")
if answer == "7" or answer.lower() == "seven":
    print("Correct! You move on to the next question.\n")
else:
    print("Wrong answer. Game over!")
    exit()

# Question 8
answer = input("8. What is the chemical symbol for water? ").upper()
if answer == "H2O":
    print("Correct! You move on to the next question.\n")
else:
    print("Wrong answer. Game over!")
    exit()

# Question 9
answer = input("9. Who painted the Mona Lisa? ").lower()
if answer == "leonardo da vinci" or answer == "da vinci":
    print("Correct! You move on to the final question.\n")
else:
    print("Wrong answer. Game over!")
    exit()

# Question 10
answer = input("10. What is the fastest land animal? ").lower()
if answer == "cheetah":
    print("Congratulations! You found the treasure!")
else:
    print("Wrong answer. Game over!")

