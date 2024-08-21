print('in this adv. calculator we can split bill in percentages')
people = int(input("Enter the number of people: "))
total = int(input("Enter the total amount: "))
for i in range(people):
    percentage = float(input(f"Enter the percentage share for person {i+1}:"))
    a = (percentage / 100) * total
    print(f"person {i+1} have to pay: {a}")





