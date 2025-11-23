import random

print("🎯 Guess the Number Game!")
print("Choose a difficulty level:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-200)")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    max_range = 50
elif choice == "2":
    max_range = 100
elif choice == "3":
    max_range = 200
else:
    print("Invalid choice! Defaulting to Medium.")
    max_range = 100

secret_number = random.randint(1, max_range)
attempts = 0
guess = None

print(f"\nI'm thinking of a number between 1 and {max_range}.")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high! Try again.\n")
    elif guess < secret_number:
        print("Too low! Try again.\n")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
