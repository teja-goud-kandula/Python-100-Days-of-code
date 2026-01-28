import random

game_images = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,  # Rock
    """
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """,  # Paper
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """   # Scissors
]

""" 
Official rules of the game

    Rock defeats Scissors.
    Scissors defeat Paper.
    Paper defeats Rock.

"""

choice = ["Rock", "Paper", "Scissors"]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
print(f"Your choice: {choice[your_choice]}\n {game_images[your_choice]}")
your_choice = choice[your_choice]


computer_choice = random.randint(0, 2)
print(f"Your choice: {choice[computer_choice]}\n {game_images[computer_choice]}")
computer_choice = choice[computer_choice]


if your_choice == computer_choice:
    print("It's a draw.")
elif your_choice == 'Rock' and computer_choice == 'Scissors':
    print("You won!")
elif your_choice == 'Rock' and computer_choice == 'Paper':
    print("Computer won!")
elif your_choice == 'Scissors' and computer_choice == 'Rock':
    print("Computer won!")
elif your_choice == 'Scissors' and computer_choice == 'Paper':
    print("You won!")
elif your_choice == 'Paper' and computer_choice == 'Rock':
    print("You won!")
elif your_choice == 'Paper' and computer_choice == 'Scissors':
    print("Computer won!")
else:
    print("Wrong inputs may be!, just a else statement!")
