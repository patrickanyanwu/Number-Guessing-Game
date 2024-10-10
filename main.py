from art import logo
import random
print(logo)
correct_number = random.randint(1, 100)
print("Welcome to Number Guessing Game!")
print("Im thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = -1
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

def guess(att):
    print(f"You have {att} attempts remaining to guess the correct number.")
    guess_num = int(input("Make a guess: "))
    if guess_num < correct_number:
        print("Too low.")
    elif guess_num > correct_number:
        print("Too high.")
    elif guess_num == correct_number:
        print(f"Correct! {correct_number} was the number i was thinking of.")
        return True
    print("Guess again.")
    return False


while attempts > 0:
    if guess(attempts):
        break
    attempts -= 1
if attempts == 0:
    print("You ran out of guesses, you lose!")