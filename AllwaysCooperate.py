#an example bot
class AllwaysCooperate:
    def __init__(self):
        self.name = "AllwaysCooperate"
        self.description = "This bot allways cooperates."
        self.defaultAction = "cooperate"
        self.action = self.defaultAction
        self.score = 0

    def defect(self):
        self.action = "defect"

    def cooperate(self):
        self.action = "cooperate"

    def respond(self, opposingAction):
        self.cooperate()