import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number=random.randint(1,100)

def game(lives,number):
  while lives > 0:  
    print(f"You have {lives} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
        lives-= 1
    elif guess < number:
        print("Too low.")
        lives-= 1
    else:
        print(f"You got it! The answer was {number}.")
        break
  
  if lives==0:
    print("You've run out of guesses, you lose.")

if difficulty == "easy":
    lives = 10
    game(lives,number)
elif difficulty == "hard":
    lives = 5
    game(lives,number)

