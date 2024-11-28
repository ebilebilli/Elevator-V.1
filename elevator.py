from random import choice
from message_to_user import up_message, down_message, opening, closing

building_floors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
passenger_names = ['Leyla', 'Arif', 'Zahir']

class Elevator:
    def __init__(self, building_floor_size: list[int] ):
        self.building_floor_size = building_floor_size
        self.limit = 10
        self.current_floor = choice(building_floors)
        
    def elevator_up_side(self, target):
            self.current_floor = self.current_floor + target

    def elevator_down_side(self, target):
            self.current_floor = self.current_floor - target
            
    def up(self):
            print(up_message)    

    def down(self):
            print(down_message)        

    def opening(self):
            print(opening)
    
    def closing(self):
            print(closing)

building_elevator = Elevator(building_floors)


