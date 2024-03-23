import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_image = [rock, paper, scissors]
computer = random.randint(0, 2)
# print(f"Computer chooses: {computer}")


player_one = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if player_one >= 3 or player_one < 0:
    print("You typed an invalid number, you lose!")
else:

    if computer == 0:
        if player_one == 0:
            print("Draw")
            print(f"Your choice: {game_image[0]}")
            print(f"The Computer choosed: {game_image[0]}")

        elif player_one == 1:
            print("You win")
            print(f"Your choice: {game_image[1]}")
            print(f"The Computer choosed: {game_image[0]}")
        else:
            print("You lost the Game. Computer win.")
            print(f"Your choice: {game_image[2]}")
            print(f"The Computer choosed: {game_image[0]}")
    elif computer == 1:
        if player_one == 0:
            print("You lost the Game. Computer win.")
            print(f"Your choice: {game_image[0]}")
            print(f"The Computer choosed: {game_image[1]}")
        elif player_one == 1:
            print("Draw")
            print(f"Your choice: {game_image[1]}")
            print(f"The Computer choosed: {game_image[1]}")
        else:
            print("You win.")
            print(f"Your choice: {game_image[2]}")
            print(f"The Computer choosed: {game_image[1]}")
    else:
        if player_one == 0:
            print("You win")
            print(f"Your choice: {game_image[0]}")
            print(f"The Computer choosed: {game_image[2]}")
        elif player_one == 1:
            print("Computer win")
            print(f"Your choice: {game_image[1]}")
            print(f"The Computer choosed: {game_image[2]}")
        else:
            print("Draw.")
            print(f"Your choice: {game_image[2]}")
            print(f"The Computer choosed: {game_image[2]}")
