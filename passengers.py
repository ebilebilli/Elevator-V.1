import random
from elevator import building_floors, passenger_names

class Passengers:
    def __init__(self,passanger: list[str], current_floor: int, target_floor: int):
        self.passangers = passanger
        self.current_floor = current_floor
        self.target_floor = target_floor

passenger_example = Passengers(random.choice(passenger_names), random.choice(building_floors), random.choice(building_floors))

