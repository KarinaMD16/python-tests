import random

min= int(input("Enter the lowest number: "))
max = int(input("Enter the highest number: "))

limit =int(input("Enter the number of attempts: "))
n = random.randint(min, max)
counter = 0

while counter < limit:
    try:
        guess = int(input(f"Guess the number between {min} and {max}: "))

        if guess < n:
            print("Too low! Try again. ")
            counter+= 1

        elif guess > n:
            print("Too high! Try again. ")
            counter+= 1

        else:
            print("Congratulations! You guessed the number. It took you " + str(counter) + " tries.")
            break
        
    except ValueError:
        print(f"Invalid input. Please enter a number between {min} and {max}.")