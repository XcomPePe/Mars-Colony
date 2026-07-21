#colony.py

from colonist import Colonist

class Colony:
    def __init__(self, name):
        self.name = name
        self.oxygen = 50
        self.food = 50
        self.energy = 50
        self.chicks = "few"
        self.day = 1
        self.population = 0
        self.colonists: list[Colonist] = []

    def show_status(self):
        print(f"=== {self.name} ===")
        print(f"Day: {self.day}")
        print(f"Oxygen: {self.oxygen}")
        print(f"Food: {self.food}")
        print(f"Energy: {self.energy}")
        print(f"Chicks: {self.chicks}")
        print(f"Population:", len(self.colonists))
    
    def next_day(self):
        self.day += 1
        self.energy -= 1
        for colonist in self.colonists:
            colonist.change_colony_state(self)

    def add_colonist(self, colonist):
        self.colonists.append(colonist)
        
    def show_colonists(self):
        for colonist in self.colonists:
            print(colonist.name)
            print(colonist.job)
            print(colonist.age)
            print(colonist.health)