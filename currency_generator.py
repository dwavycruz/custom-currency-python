import random

currency_values = [2, 100, 1000]

people_on_bills = [
    "Christopher ford",
    "Johnny Lopez",
    "Avery Sadie",
    "Cruz Rivera"
]

print("Custom Currency Generator\n")

for value in currency_values:
    person = random.choice(people_on_bills)

    print("------------------------------")
    print(f"Bill Value: {value} dollars")
    print(f"Featured Person: {person}")
    print("------------------------------\n")