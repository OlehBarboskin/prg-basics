import random

number_to_guess = random.randint(1,100)
user_guess = 0

print("Guess the number between 1 and 100")

while user_guess != number_to_guess:
    user_guess = int(input("Enter a number to guess: "))
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You did it!")
    