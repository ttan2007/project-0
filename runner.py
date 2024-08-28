import Player from 'player.py'
import Item from 'item.py'
import Character from 'character.py'
import playGame from 'wordle.py'
print("Welcome to my game!")
player_name = input("What is your name?") 
player = Player(player_name, 100)

decision1 = input("You come up to a big field. You see a star. It looks scary. Do you pick it up? (Y/N): ")
if decision1 == "Y":
    star = Item("star", "A shiny star")
    player.inventory.append(star)

else: 
    decision2 = input("You leave the star behind. Do you want to go to the forest? (Y/N): ")

