class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.received = False
        self.inventory = []

    def talk_to_player(self, player_name):

        if self.received == False:
            print(f"{self.name} says: Hi {player_name}. I am looking for a star. Do you have one for me?")
            YN = input("Do you have a star? (Y/N): ")
            if YN == "Y":
                self.receive_item(player.inventory["star"])
                player.inventory.remove(player.inventory["star"])
                
            else:
                print(self.name + "Says Keep looking")
            
        else: 
            print(self.name + "says: I already have one go away!")

    def receive_item(self, item):
        self.received = True
        self.append(item)
        print(f"{self.name} says: Thank you for the {item.name} I will treasure it forever!")