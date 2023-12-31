from time import sleep

from MyBot import MyBot
from AllwaysDefect import AllwaysDefect
from AllwaysCooperate import AllwaysCooperate

good = "cooperate"
bad = "defect"


#Change this if you want to
bot1 = AllwaysCooperate()
bot2 = MyBot()

print(bot1.name + " | " + bot1.description + " | " + bot1.defaultAction)
print(bot2.name + " | " + bot2.description + " | " + bot2.defaultAction)

#adds the scores.
def evaluate(action1, action2):
    if action1 == good and action2 == good:
        bot1.score += 2# Print initial information about each bot
        bot2.score += 2
    elif action1 == bad and action2 == good:
        bot1.score += 3
        bot2.score += 0
    elif action1 == good and action2 == bad:
        bot1.score += 0
        bot2.score += 3
    elif action1 == bad and action2 == bad:
        bot1.score += 1
        bot2.score += 1

#simulate interactions between bots.
for i in range(1,101):
    sleep(0.1)
    evaluate(bot1.action, bot2.action)
    print(i, "Bot1", bot1.action ,bot1.score ,"|" , "Bot2", bot2.action , bot2.score)
    bot1.respond(bot2.action)
    bot2.respond(bot1.action)
print(bot1.name ,bot1.score)
print(bot2.name, bot2.score)
