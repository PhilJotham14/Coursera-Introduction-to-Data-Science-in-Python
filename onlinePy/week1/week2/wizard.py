class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        # self.name = name
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, house, subject):
        # self.name = name
        super().__init__(name)
        # self.house = house
        self.subject = subject


wizard = Wizard("Albus")
student = Student("Harry")
# professor = Professor("Guiplao")
