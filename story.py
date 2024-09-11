def start_your_trip():
    pass
from player import Player
from wordle import playGame
from inventory import Inventory
from fight import combat, attack
import random
from character import Character
from inventory import Inventory 

def start_your_trip():

    player1 = Player("", 100) 
    player1.name = input("Hello, what is your name? ")

    print(f"Welcome, {player1.name}, to your adventure.")
    print("You wake up in an empty field with no memory of how you got there.")
    print("Suddenly, a man approaches you with a grin on his face.")
    print("'Hey there! How about a game of rock-paper-scissors?'")
    
    choice = input("Do you want to play rock-paper-scissors or fight him? (play/fight) ").lower()
    
    if choice == "play":
        play_rock_paper_scissors(player1)
    elif choice == "fight":
        combat(player1, "Mysterious Man", 100)
    else:
        print("You decide not to interact. The man walks away, leaving you alone.")
    
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
        print("It's a tie! You both chose the same thing. The man laughs like a maniac.")
        play_rock_paper_scissors(player)  
    elif (player_choice == "rock" and man_choice == "scissors") or \
         (player_choice == "scissors" and man_choice == "paper") or \
         (player_choice == "paper" and man_choice == "rock"):
        print("You win the game!")
        give_special_item(player)
    else:
        print("You lost. The man frowns in disappointment.")

def give_special_item(player):
    special_item = "Shiny Amulet"
    player.add_item(special_item)
    print(f"The man hands you a {special_item}. He says, 'Hold on to this...'")
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

def run_away(player):
    print("You run away from the graveyard back to the field.")
    start_your_trip()

def start_quest(player):
    print("Jeb: There’s a gate at the end of this graveyard, but it’s locked by an old puzzle.")
    print("Could you please help me open it?")
    choice = input("Y or N? ").upper()
    
    if choice == "Y":
        play_puzzle(player)
    else:
        print("You decline to solve the puzzle. Jeb is sad.")
        start_your_trip()

def play_puzzle(player):
    print("Jeb pats you on the back. 'Go on then Boy!', he says.")
    print("After a while of searching you reach the gate.")
    success = playGame("START")
    print(f"Debug: Puzzle success = {success}")

    if success:
        print("You solved the puzzle and opened the gate!")
    else:
        print("You failed the puzzle and lose 50 health points.")
        player.health -= 50
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
    
    action = input("Do you give him the amulet or attack him? (give/attack): ").lower()
    
    if action == "give" and "Shiny Amulet" in player.inventory:
        print("You hand the boy the Shiny Amulet. He smiles and gives you a strange key in return.")
        player.remove_item("Shiny Amulet")
        player.add_item("Strange Key")
        print("You put the Strange Key in your inventory. It might be useful later!")
    elif action == "give" and "Shiny Amulet" not in player.inventory:
        print("You don't have anything interesting to give the boy.")
    elif action == "attack":
        print("The boy looks shocked as you prepare to attack him!")
        combat(player, "Young Boy", 50)
    else:
        print("Invalid choice. You stand there awkwardly.")

def game_over(player):
    print(f"Game over! {player.name} has perished.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        start_your_trip()
    else:
        print("Thanks for playing!")

start_your_trip()
