import random
from elevator import building_floors

class Passengers:
    def __init__(self,passanger):
        self.passangers = passanger
        self.current_floor = random.choice(building_floors)
        self.target_floor = random.choice(building_floors)

passenger_example_one = Passengers('Leyla')
passenger_example_two = Passengers('Nigar')






