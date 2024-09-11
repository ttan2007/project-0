import random


def combat(player, opponent_name, opponent_health):
    print(f"{opponent_name} challenges you to a fight!")
    
    while player.health > 0 and opponent_health > 0:
        print(f"\nYour Health: {player.health}, {opponent_name}'s Health: {opponent_health}")
        action = input("Choose your action (attack/block/dodge/countermove): ").lower()

        opponent_action = random.choice(["attack", "block", "dodge", "countermove"])
        print(f"The {opponent_name} chooses to {opponent_action}.")

        if action == "attack":
            if opponent_action == "dodge":
                print(f"{opponent_name} dodges your attack!")
            elif opponent_action == "block":
                print(f"{opponent_name} blocks your attack!")
            else:
                damage = random.randint(15, 25)
                opponent_health -= damage
                print(f"You hit {opponent_name} for {damage} damage!")
        elif action == "block":
            print("You prepare to block.")
        elif action == "dodge":
            print("You try to dodge the next attack.")
        elif action == "countermove":
            if opponent_action == "attack":
                damage = random.randint(20, 30)
                opponent_health -= damage
                print(f"You successfully countered {opponent_name}'s attack and dealt {damage} damage!")
            else:
                print(f"You tried to counter but {opponent_name} didn't attack.")
        else:
            print("Invalid action, you lose your turn.")

        if opponent_action == "attack":
            if action == "dodge":
                print("You dodge the opponent's attack!")
            elif action == "block":
                print("You block the opponent's attack!")
            else:
                damage = random.randint(10, 20)
                player.health -= damage
                print(f"{opponent_name} hits you for {damage} damage!")

    if player.health > 0:
        print(f"\nYou defeated {opponent_name}!")
        collect_loot(player)
    else:
        print(f"\nYou were defeated by {opponent_name}.")
        game_over(player)

def attack(player, damage):
    print(f"Jeb attacks you! You lose {damage} health points.")
    player.health -= damage 
    print(f"Your health is now {player.health}.")
    
    if player.health <= 0:
        game_over(player)  
    else:
        print("You barely escape the graveyard.")
        start_your_trip()
