# libraries in short abiloity to use existing or your code in another project
import random
# from random import choice

# # double quotes since they are strings
# # random.choice takes up items in a list and randomly chooses one for you
# #  incase you "from random" only their is no need to use random.choice you can use choice only
# # coin = random.choice(["heads", "tails"])
# coin = choice(["heads", "tails"])
# print(coin)

# number = random.ram(1,10)
# print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
