import random

secret_number = random.randint(1, 10)
attempts = 3

print("Welcome to Number Guessing Game!")
print(f"You have {attempts} attempts to guess the number (between 1 and 10).")

while attempts > 0:
    user_guess = int(input("Enter your guess: "))

    if user_guess == secret_number:
        print(f"Congratulations! You've guessed the number ({secret_number})!")
        break
    elif user_guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    attempts -= 1

if attempts == 0:
    print(f"Sorry, you've run out of attempts. The number was: {secret_number}")