# Object Oriented Programming
# An object of a class is identified by the keyword 'is a'
# A class of an object is defined by the keyword class followed by the name of the class

class Car:
    pass

# the word pass is a phrase word 'to ignore' in python


print(Car())

nissan = Car()
toyota = Car()
subaru = Car()
mitsubishi = Car()
ford = Car()

print(nissan == toyota)

# Defining a class with properties, attributes or characteristics
# In python, defining properties or structures of an object we use the __init__ method


class Phone:
    def __init__(self, name1, model1, color1, price1):
        self.name = name1
        self.model = model1
        self.color = color1
        self.price = price1


# print(Phone())
tecno = Phone('tecno', 'Camon15', 'blue', 700000)
samsung = Phone('samsung', 'galaxyprime', 'white', 800000)
iphone = Phone('iphone', '12', 'grey', 1800000)
tecno.price = 1000000
print(tecno.name)
print(tecno.price)
# as a rule in python the first attribute of any object in class is self, the keywors self is used to
# identify the properties of an object name, color, model and price are parameters to be assigned to the property of the class.
