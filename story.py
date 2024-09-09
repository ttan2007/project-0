from player import Player
from wordle import playGame

def start_your_trip():
    player1 = Player("", 100)
    player1.name = input("Hello what is your name? ")

    print(f"Welcome {player1.name} to your adventure")
    print("You wake up in an empty field without any memory of how you got there.")
    print("Your head is pounding and you see nothing but grass surrounding you.")
    print("Up ahead you notice a sign that reads 'Graveyard 5 miles North'.") 
    print("Behind you read a sign that reads 'Sludge Swamp 10 miles South'." )
    choice = input("Do you want to go up north or down south? (north/south) ")
    if choice == "north":
        go_north()
    elif choice == "south":
        go_right()

def go_north():
    print("You walk into the ominous graveyard. ")
    print("You run into an old man holding a lantern and a shovel. ")
    choice = input("Do you talk to him or run away? (talk/run)")
    if choice == "talk":
        talk()
    elif choice == "run":
        run()

def talk():
    print("Old man: Hello.. my name is Jeb. ")

    ## print("On the horizon, you see a rusted gate clouded by a sea of deep fog.")
    ## print("Do you wish to solve the puzzle?")
    ## choice = input("Y or N ").upper()
    ## if choice == "Y":
    ##     playGame("START")
    ## elif choice == "N":
    ##     print("Come again when you're ready.")
    ## else:
    ##     print("Invalid input. Please enter Y or N.")

start_your_trip()