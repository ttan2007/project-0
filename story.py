from player import Player
from wordle import playGame

player1 = Player("", 100)
player1.name = input("Hello what is your name")

print("Weclome " + player1.name + "to your adventre")
playGame("START")