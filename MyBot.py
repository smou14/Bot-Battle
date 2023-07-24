import random
class MyBot:
    # Change the strings to whatever you want.
    def __init__(self):
        self.name = "My Bot"
        self.description = "This is the player's custom bot."
        self.defaultAction = "defend"
        self.action = self.defaultAction
        self.score = 0

    def attack(self):
        self.action = "attack"

    def defend(self):
        self.action = "defend"

    # Keep this func please, you can change the logic though.
    def respond(self, opposingAction):
        if random.randrange(1,10) > 1:
            self.defend()
        else:
            self.attack()