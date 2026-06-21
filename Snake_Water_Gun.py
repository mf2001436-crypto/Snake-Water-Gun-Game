# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. 

import random
print("-----------Welcome to snake, water, gun Game!-----------")
choice = input("Enter your choice(snake, water, gun): ")
computer_choice = random.choice(["snake", "water", "gun"])
print(f"Computer choose : {computer_choice}")
if choice == computer_choice:
    print("Draw")
elif choice == "snake" and computer_choice == "water":
    print("You win")
elif choice == "water" and computer_choice == "gun":
    print("You win")
elif choice == "gun" and computer_choice == "snake":
    print("You win")
else:
    print("You lose")