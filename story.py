import random
from player import Player
from wordle import playGame
from item import Item

# Inventory system
inventory = []

def start_your_trip():
    player1 = Player("", 100) 
    player1.name = input("Hello, what is your name? ")

    print(f"Welcome, {player1.name}, to your adventure.")
    print("You wake up in an empty field with no memory of how you got there.")
    print("Suddenly, a man approaches you with a grin on his face.")
    print("'Hey there! How about a game of rock-paper-scissors?'")
    
    choice = input("Do you want to play rock-paper-scissors with the man? (yes/no) ").lower()
    
    if choice == "yes":
        play_rock_paper_scissors(player1)
    else:
        print("You decide not to play. The man walks away, leaving you alone.")
    
    print("Ahead of you, a sign reads 'Graveyard 5 miles North'.")
    print("Behind you, a sign reads 'Sludge Swamp 10 miles South'.")
    choice = input("Do you want to go North or South? (north/south) ").lower()
    
    if choice == "north":
        go_north(player1)
    elif choice == "south":
        go_south(player1)
    else:
        print("Invalid choice. Please choose north or south.")
        start_your_trip()

def play_rock_paper_scissors(player):
    options = ["rock", "paper", "scissors"]
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    man_choice = random.choice(options)
    
    print(f"The man chooses {man_choice}.")
    
    if player_choice == man_choice:
        print("It's a tie! You both chose the same thing.")
        play_rock_paper_scissors(player)  # Play again if there's a tie
    elif (player_choice == "rock" and man_choice == "scissors") or \
         (player_choice == "scissors" and man_choice == "paper") or \
         (player_choice == "paper" and man_choice == "rock"):
        print("You win the game!")
        give_special_item(player)
    else:
        print("You lost the game. Better luck next time!")

def give_special_item(player):
    special_item = "Shiny Amulet"
    inventory.append(special_item)
    print(f"The man hands you a {special_item}. He says, 'This might come in handy later!'")
    print("You put the amulet in your inventory.")

def go_north(player):
    print("You walk into the ominous graveyard.")
    print("You run into an old man holding a lantern and a shovel.")
    choice = input("Do you talk to him or run away? (talk/run) ").lower()

    if choice == "talk":
        talk(player)
    elif choice == "run":
        run_away(player)
    else:
        print("Invalid input.")
        go_north(player)

def talk(player):
    print("Old man: Hello.. my name is Jeb. Can you help me with a task?")
    choice = input("Do you agree to help Jeb? (Y/N) ").upper()
    
    if choice == "Y":
        start_quest(player)
    elif choice == "N":
        print("Jeb looks disappointed. He swings his shovel at you!")
        attack(player, 20)  
    else:
        print("Invalid input.")
        talk(player)

def attack(player, damage):
    print(f"Jeb attacks you! You lose {damage} health points.")
    player.health -= damage 
    print(f"Your health is now {player.health}.")
    
    if player.health <= 0:
        game_over(player)  
    else:
        print("You barely escape the graveyard.")
        start_your_trip()

def run_away(player):
    print("You run away from the graveyard back to the field.")
    start_your_trip()

def start_quest(player):
    print("Jeb: There’s a gate at the end of this graveyard, but it’s locked by a puzzle.")
    print("Would you like to attempt the puzzle?")
    choice = input("Y or N? ").upper()
    
    if choice == "Y":
        play_puzzle(player)
    else:
        print("You decline to solve the puzzle. Jeb is sad.")
        start_your_trip()

def play_puzzle(player):
    print("You must solve a Wordle-like puzzle to open the gate.")
    success = playGame("START")  

    if success:
        print("You solved the puzzle and opened the gate!")
    else:
        print("You failed the puzzle and lose 15 health points.")
        player.health -= 15  
        print(f"Your health is now {player.health}.")
        
        if player.health <= 0:
            game_over(player) 
        else:
            start_your_trip()

def go_south(player):
    print("You head towards the Sludge Swamp.")
    print("A thick, unpleasant smell fills the air.")
    print("You can barely see anything.")
    print("You see a dim light at the other end of the lake.")
    print("You decide to start swimming towards the light.")
    print("As you get closer you notice it's a small boat!")
    choice = input("Do you climb aboard or sneak around it? (climb/sneak)").lower()
    
    if choice == "climb":
        print("You run into a startled young boy who was out fishing!")
        interact_with_boy(player)
    elif choice == "sneak":
        print("Slowly, you notice that there is a young boy aboard who is fishing.")
        interact_with_boy(player)
    else:
        print("Invalid choice.")
        go_south(player)

def interact_with_boy(player):
    print("The young boy notices you and asks if you have anything interesting.")
    if "Shiny Amulet" in inventory:
        print("You hand the boy the Shiny Amulet. He smiles and gives you a strange key in return.")
        inventory.remove("Shiny Amulet")
        inventory.append("Strange Key")
        print("You put the Strange Key in your inventory. It might be useful later!")
    else:
        print("You don't have anything to give the boy.")

def examine(item):
    if item in inventory:
        print(f"You examine the {item}.")
    else:
        print(f"You don't have {item} in your inventory.")

def take(item):
    print(f"You take the {item}.")
    inventory.append(item)

def game_over(player):
    print(f"Game Over, {player.name}. You have lost all your health.")
    print("Better luck next time!")
    exit() 

start_your_trip()
