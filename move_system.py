from time import sleep
from elevator import Elevator
from passengers import Passengers
from message_to_user import enter_message

def elevator_down_system(person: Passengers, elevator: Elevator):
    while elevator.current_floor > person.current_floor:
        elevator.elevator_down_side(1)
        print(f'{elevator.current_floor}--[]')
        sleep(1.2)

    if elevator.current_floor == person.current_floor:
        elevator.opening()
        print(f'{person.passangers} {enter_message}')
        elevator.closing()


def elevator_up_system(person: Passengers, elevator: Elevator):
    while elevator.current_floor < person.current_floor:
        elevator.elevator_up_side(1)
        print(f'{elevator.current_floor}--[]')
        sleep(1.2)

    if elevator.current_floor == person.current_floor:
        elevator.opening()
        print(f'{person.passangers} {enter_message}')
        elevator.closing()
