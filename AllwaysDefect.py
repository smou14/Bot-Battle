#an example bot
class AllwaysDefect:
    def __init__(self):
        self.name = "AllwaysDefect"
        self.description = "This bot allways defects."
        self.defaultAction = "defect"
        self.action = self.defaultAction
        self.score = 0

    def defect(self):
        self.action = "defect"

    def cooperate(self):
        self.action = "cooperate"

    def respond(self, opposingAction):
        self.defect()