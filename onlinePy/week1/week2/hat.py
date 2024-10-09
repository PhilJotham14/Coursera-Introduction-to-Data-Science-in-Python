# Implements sort() with a class method
import random


class Hat:
    # def __init__(self):
    houses = ["Gryfindor", "HUddlepuff", "Ravenclaw", "Slythariz"]

    @classmethod
    # def sort(self, name):
    def sort(cls, name):
        # print[name, "is in", random.choice(self.houses)]
        print(name, "is in", random.choice(cls.houses))


# hat = Hat()
# hat.sort("Harry")
Hat.sort("Harry")
