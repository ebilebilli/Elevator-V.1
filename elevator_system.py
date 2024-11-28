from elevator import Elevator, building_elevator
from passengers import Passengers, passenger_example
from move_system import elevator_down_system, elevator_up_system
from move_with_passenger import elevator_move_with_passanger
from os import system

def elevator_system(person: Passengers, elevator: Elevator):
    if person.current_floor > elevator.current_floor:
        elevator.up()                                                   
        elevator_up_system(person, building_elevator)
        elevator_move_with_passanger(person, elevator)
        

    elif person.current_floor == elevator.current_floor:
        elevator.opening()
        elevator.closing()
    
    elif person.current_floor < elevator.current_floor:
        elevator.down()
        elevator_down_system(person, elevator)
        elevator_move_with_passanger(person, elevator)

elevator_system(passenger_example, building_elevator)      