
from art import logo
import random 
print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
print('submit a guess for a number between 1 and 100.')
number = random.choice(range(1,101))
print(f"Guessing number is {number} \n")
select_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

guessing_lives = 0

if select_difficulty == "hard" :
    guessing_lives = 5
    print(f"you got {guessing_lives} guesses to guess a right number.")
elif select_difficulty == "easy":
    guessing_lives = 10
    print(f"you got {guessing_lives} guesses to guess a right number.")


while guessing_lives > 0:
    guess_number = int(input("Enter your number : "))
    if guess_number == number:
        print(f"You Win, you guessed a right number {number}")
    elif guessing_lives == 1:
        print("You run out of moves.")
    elif guess_number > number:
        print("Too high")
        print(f"You have {guessing_lives-1} attempts remaining to guess the number.")
    elif guess_number < number :
        print("Too low")
        print(f"You have {guessing_lives-1} attempts remaining to guess the number.")
    
    guessing_lives -= 1 
    
    



