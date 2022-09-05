import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. :\n")
if choice == "0":
    print(rock)
elif choice == "1":
    print(paper)
elif choice == "2":
    print(scissors)
else:
    print("Invalid input")

game=[rock,paper,scissors]
computer_choice=random.randint(0,2)
print(f"Computer chose:\n{game[computer_choice]}")

if choice == "0" and computer_choice == 0:
    print("Draw")
elif choice == "0" and computer_choice == 1:
    print("You lose")
elif choice == "0" and computer_choice == 2:
    print("You win")
elif choice == "1" and computer_choice == 0:
    print("You win")
elif choice == "1" and computer_choice == 1:
    print("Draw")
elif choice == "1" and computer_choice == 2:
    print("You lose")
elif choice == "2" and computer_choice == 0:
    print("You lose")
elif choice == "2" and computer_choice == 1:
    print("You win")
elif choice == "2" and computer_choice == 2:
    print("Draw")
