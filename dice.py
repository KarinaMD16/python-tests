import random

# This file contains a simple dice rolling game, where the player 
# can choose how many dice to roll and see the results.

while True:
    choice = input("roll the dice? (y/n): ").lower()
    if choice == "y":
        amount = input("how many dice do you want to roll? ")
        for i in range(int(amount)):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f"({dice1}, {dice2})")
    elif choice == "n":
        print("Goodbye!")
        break
    else: print("Invalid input, please enter 'y' or 'n'.")