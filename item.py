class Item:
    def __init__(self, type_of_item, description):
        self.type_of_item = type_of_item
        self.description = description

        if type_of_item == "star":
            self.points = 5
        else:
            self.points = 1

    def use_item(self, player):
        player.health += self.points