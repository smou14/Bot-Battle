import random
class Attacker:
    # Change the strings to whatever you want.
    def __init__(self):
        self.name = "Attacker"
        self.description = "This bot allways attacks."
        self.defaultAction = "attack"
        self.action = self.defaultAction
        self.score = 0

    def attack(self):
        self.action = "attack"

    def defend(self):
        self.action = "defend"

    # Keep this func please, you can change the logic though.
    def respond(self, opposingAction):
        self.attack()