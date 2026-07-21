#colonist.py

class Colonist:
    def __init__(self, name, age, health, job):
        self.name = name
        self.age = age
        self.health = health
        self.job = job
    def change_colony_state(self, colony):
        colony.oxygen -= 2
        colony.food -= 2
        