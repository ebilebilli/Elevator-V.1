from random import choice
from time import sleep
from back_settings.message_to_user import up_message, down_message, opening, closing

building_floors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Elevator:
    def __init__(self, building_floor_size: list[int] ):
        self.building_floor_size = building_floor_size
        self.current_floor = choice(building_floors)
        
    def elevator_up_side(self, target):
            self.current_floor = self.current_floor + target

    def elevator_down_side(self, target):
            self.current_floor = self.current_floor - target
            
    def up(self, target):
            (f'{up_message} to floor: {target}')
            sleep(1.2)   

    def down(self, target):
            print(f'{down_message} to floor: {target}')
            sleep(1.2)

    def opening(self):
            print(opening)
            sleep(1.2)
    
    def closing(self):
            print(closing)
            sleep(1.2)

building_elevator = Elevator(building_floors)


