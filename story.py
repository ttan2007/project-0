from player import Player
from wordle import playGame

player1 = Player("", 100)
player1.name = input("Hello what is your name? ")

print(f"Welcome {player1.name} to your adventure")

print("Do you wish to solve the puzzle?")

choice = input("Y or N ").upper()
if choice == "Y":
    playGame("START")
elif choice == "N":
    print("Come again when you're ready.")
else:
    print("Invalid input. Please enter Y or N.")