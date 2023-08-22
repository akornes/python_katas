import random

user_choice = int(input("Choose 1 for rock, 2 for paper, or 3 for scissors: "))
opponent_choice = random.randint(1, 3)
print(f"Opponent chose:  {opponent_choice}")

if user_choice == opponent_choice:
    print("Tie")
elif user_choice == 1 and opponent_choice == 3:
    print("You Win")
else:
    print("You Lose")

