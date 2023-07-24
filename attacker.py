import random
class Attacker:
    # Change the strings to whatever you want.
    def __init__(self):
        self.name = "Attacker"
        self.description = "This bot allways defects."
        self.defaultAction = "defect"
        self.action = self.defaultAction
        self.score = 0

    def defect(self):
        self.action = "defect"

    def cooperate(self):
        self.action = "cooperate"

    # Keep this func please, you can change the logic though.
    def respond(self, opposingAction):
        self.defect()