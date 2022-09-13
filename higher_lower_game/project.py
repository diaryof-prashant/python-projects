import random
from game_data import data
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
print(logo)

firstp=random.choice(data)
print(f"Compare A: {firstp['name']}, a {firstp['description']}, from {firstp['country']}.")

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print(vs)
secondp=random.choice(data)
print(f"Compare B: {secondp['name']}, a {secondp['description']}, from {secondp['country']}.")

answer=input("Who has more followers? Type 'A' or 'B': ")

def compare(answer):
    if answer=='a':
        if firstp['follower_count']>secondp['follower_count']:
            print("Guessed Correctly")
        else:
            print("Guessed Incorrectly")
    elif answer=='b':
        if secondp['follower_count']>firstp['follower_count']:
            print("Guessed Correctly")
        else:
            print("Guessed Incorrectly")
compare(answer) 
