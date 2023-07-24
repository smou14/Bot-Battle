import random
class MyBot:
    # Change the strings to whatever you want.
    def __init__(self):
        self.name = "My Bot"
        self.description = "This is the player's custom bot."
        self.defaultAction = "cooperate"
        self.action = self.defaultAction
        self.score = 0

    def defect(self):
        self.action = "defect"

    def cooperate(self):
        self.action = "cooperate"

    # Keep this func please, you can change the logic though.
    def respond(self, opposingAction):
        if random.randrange(1,10) > 1:
            self.cooperate()
        else:
            self.defect()