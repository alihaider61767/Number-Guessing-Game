import random

print("Welcome to Number Guessing Game")
print("I am thinking of a number between 1 and 100")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts")
        break 