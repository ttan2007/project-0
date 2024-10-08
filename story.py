# Import necessary modules and classes
import random
from player import Player
from wordle import playGame
from inventory import Inventory
from fight import combat, attack
from character import Character
from inventory import Inventory 

def start_your_trip():
    # Initialize the player with a name and 100 health points
    player = Player("", 100) 
    player.name = input("Enter your name to start. ")

    # Introduction sequence
    print(f"Your eyes open slowly, and you feel your head pounding. Your vision is blurry and one word echoes through your mind, {player.name}, {player.name}, {player.name}, {player.name}... ")
    print("You collapse.")
    print("Once again, your eyes slowly open while you adjust to the sunlight. You find yourself now in an empty field with no memory of how you got there.")
    print("Heavy footsteps suddenly arise from the road behind you. You turn your head and see a man with a giant pitchfork in his hand and an equally giant cigar in his mouth. He approaches you with an eerie grin on his face.")
    print("Mysterious Man: Haven't seen you around..")
    
    # Player's first choice
    choice = input("Mysterious Man: Where do you come from stranger? (Field/Lie) ").lower()
    
    # Handle player's choice
    if choice == "field":
        print("I live here on the Field!")
        print("Mysterious Man: That don't make sense.. I own this field. He raises his pitchfork.")
        combat(player, "Mysterious Man", 100)
        go(player)
    elif choice == "lie":
        print("I live down the road...")
        print("Mystery Man: Huh.. better be back before nightfall then.")
    else:
        print("The Mysterious Man looks confused by your response.")

    # Introduce Lancer and offer a game
    print("Mysterious Man: The names Lancer.")
    print("Lancer: I love me a fun game with a new stranger. Fancy a game of rock paper scissors? I never lose. If you win I might just give you a little reward...")

    # Player's second choice
    choice = input("Do you choose to play rock-paper-scissors or choose to fight him for the reward? (play/fight) ").lower()
    
    # Handle player's second choice
    if choice == "play":
        play_rock_paper_scissors(player)
        go(player)
    elif choice == "fight":
        combat(player, "Mysterious Man", 100)
        go(player)
    else:
        print("You decide not to interact. The man walks away, leaving you alone.")
        go(player)

def go(player):
    # Player chooses direction
    choice = input("Ahead of you, a sign reads 'Graveyard 5 miles North. Behind you, a sign reads 'Sludge Swamp 10 miles South. Do you want to go North or South? (north/south) ").lower()
    
    if choice == "north":
        go_north(player)
    elif choice == "south":
        go_south(player)
    else:
        print("Invalid choice. Please choose north or south.")
        start_your_trip()

def play_rock_paper_scissors(player):
    # Rock-paper-scissors game logic
    options = ["rock", "paper", "scissors"]
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    man_choice = random.choice(options)
    
    print(f"Lancer chooses {man_choice}.")
    
    # Determine winner
    if player_choice == man_choice:
        print("It's a tie! You both chose the same thing. Lancer laughs like a maniac.")
        play_rock_paper_scissors(player)  # Play again if tie
    elif (player_choice == "rock" and man_choice == "scissors") or \
         (player_choice == "scissors" and man_choice == "paper") or \
         (player_choice == "paper" and man_choice == "rock"):
        print("You win!")
        give_special_item(player)
    else:
        print("You lost. Lancer frowns in disappointment.")

def give_special_item(player):
    # Give player a special item after winning
    special_item = "Rusty old necklace"
    player.add_item(special_item)
    print(f"Lancer hands you a {special_item}. He says, 'Hold on to this...'")
    print("Rusty old necklace.")

def go_north(player):
    # Graveyard scenario
    print("You walk into the ominous graveyard.")
    print("You run into an old man holding a lantern and a shovel.")
    print("He looks deranged by the looks of it, clothes ripped and hair and beard growing wildly.")
    choice = input("Do you talk to him or run away? (talk/run) ").lower()

    if choice == "talk":
        talk(player)
    elif choice == "run":
        run_away(player)
    else:
        print("Invalid input.")
        go_north(player)

def talk(player):
    # Jeb introduces himself and asks for help
    print("Old man: Hello stranger.. my name is Jeb. Can you help me with a task?")
    
    # Player chooses whether to help Jeb
    choice = input("Do you agree to help Jeb? (Y/N) ").upper()
    
    if choice == "Y":
        # If player agrees, start the quest
        start_quest(player)
    elif choice == "N":
        # If player refuses, Jeb attacks
        print("Jeb looks disappointed. He swings his shovel at you!")
        attack(player, 100, start_your_trip)
    else:
        # Handle invalid input by recursively calling the function
        print("Invalid input.")
        talk(player)

def run_away(player):
    # Player attempts to run, but Jeb catches and attacks
    print("You try to run away but Jeb catches you and swings his shovel at you!")
    attack(player, 100, start_your_trip)

def start_quest(player):
    # Jeb explains the quest
    print("Jeb: There's a gate at the end of this graveyard, but it's locked by an old puzzle.")
    print("Could you please help me open it?")
    
    # Player chooses whether to help with the puzzle
    choice = input("Y or N? ").upper()
    
    if choice == "Y":
        # If player agrees, start the puzzle
        play_puzzle(player)
    else:
        # If player refuses, Jeb attacks
        print("Jeb looks disappointed. He swings his shovel at you!")
        attack(player, 100, start_your_trip)

def play_puzzle(player):
    # Jeb encourages the player and they reach the gate
    print("Jeb pats you on the back. 'Go on then Boy!', he says.")
    print("After a while of searching you reach the gate.")
    
    # Player attempts to solve the puzzle
    success = playGame("START")
    
    if success:
        # If puzzle is solved, open the gate
        print("You solved the puzzle and opened the gate!")
        unlock_gate(player)
    else:
        # If puzzle fails, player loses health
        print("You failed the puzzle and lose 50 health points.")
        player.health -= 50
        print(f"Your health is now {player.health}.")
        
        # Check if player's health has reached zero
        if player.health <= 0:
            game_over(player)
        else:
            # If player still has health, restart the trip
            start_your_trip()

def unlock_gate(player):
    # Define a special item for the player to find
    special_item = "Mysterious water chalice"
    # Add the special item to the player's inventory
    player.add_item(special_item)
    # Describe the scene after unlocking the gate
    print(f"The word puzzle falls to the ground as the gate opens.")
    print(f"You explore the undiscovered parts of the graveyard and you reach a small fountain. In front of it, you find a {special_item} and pick it up.")
    print("You put the chalice in your inventory.")
    # Present the player with a choice
    choice = input("Do you choose to drink the water or head south? (drink/south) ").lower()
    if choice == "drink":
        drink()
    elif choice == "south":
        go_south(player)
    else:
        print("Invalid choice. Please choose north or south.")
        start_your_trip()

def drink():
    # Describe the effects of drinking the water
    print("You drink the shimmering water and fall to your knees. You clutch to your stomach as the water burns your insides. Suddenly your head is filled with memories of your past as they flash before your eyes. Memories of another world where you were once a prince, a life of luxury and power. But you were also a prisoner, a prisoner of your own mind.")
    print("You hear a voice in your head. It says: 'You are the chosen one. Save this world.'")
    print("You feel a surge of power flow through you and you feel a sense of purpose.")
    print("Jeb: You're a strange one. You're not like the others. You're not like me.")
    print("You look at Jeb, who is standing there, watching you.")
    print("Jeb comes closer and bows down at your feet.")
    print("To be continued...")
    print("Game Over Thank you for Playing!")

def go_south(player):
    # Describe the Sludge Swamp scenario
    print("You head towards the Sludge Swamp.")
    print("A thick, unpleasant smell fills the air.")
    print("You can barely see anything.")
    print("You see a dim light at the other end of the lake.")
    print("You decide to start swimming towards the light.")
    print("As you get closer you notice it's a small boat!")
    # Present the player with a choice
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
    # Describe the interaction with the boy
    print("The young boy notices you and asks if you have anything interesting.")
    
    # Present the player with a choice
    action = input("Do you give him the necklace or attack him? (give/attack): ").lower()
    
    if action == "give" and "Rusty old necklace" in player.inventory:
        # Handle giving the necklace
        print("You hand the boy the necklace. He smiles and gives you a strange chalice filled with shimmering water in return.")
        print("This was my dads.. he gave it to me before he died. I'm glad you found it.")
        player.remove_item("Rusty old necklace")
        player.add_item("Mysterious water chalice")
        end()
    elif action == "give" and "Mysterious water chalice" not in player.inventory:
        # Handle not having the necklace
        print("You don't have anything interesting to give the boy. Dissapointed, he tries to push you off the boat.")
        attack(player, 100, start_your_trip)  
    elif action == "attack":
        # Handle attacking the boy
        print("The boy looks shocked as you prepare to attack him!")
        combat(player, "Young Boy", 100)
        end()
    else:
        print("Invalid choice. You stand there awkwardly.")

def end():
    # Describe the ending sequence
    print("You look around the boat. In a small hidden box you find a mysterious water chalice. You impulsively have a strong urge to drink the water.")
    print("You drink the shimmering water and fall to your knees. You clutch to your stomach as the water burns your insides. Suddenly your head is filled with memories of your past as they flash before your eyes. Memories of another world where you were once a prince, a life of luxury and power. But you were also a prisoner, a prisoner of your own mind.")
    print("You hear a voice in your head. It says: 'You are the chosen one. Save this world.'")
    print("You feel a surge of power flow through you and you feel a sense of purpose.")
    print("To be continued...")
    print("Game Over Thank you for Playing!")

def game_over(player):
    # Handle the game over scenario
    print(f"Game over! {player.name} has perished.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        start_your_trip()
    else:
        print("Thanks for playing!")

# Start the game
start_your_trip()
