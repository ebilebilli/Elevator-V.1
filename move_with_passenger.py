from time import sleep
from elevator import Elevator
from passengers import Passengers
from message_to_user import exit_message

def elevator_move_with_passanger(person: Passengers, elevator: Elevator):
    if person.target_floor < elevator.current_floor:
        while elevator.current_floor > person.target_floor:
            print(f'{elevator.current_floor}--{[person.passangers]}')
            sleep(1.2)
            elevator.elevator_down_side(1)

        if elevator.current_floor == person.target_floor:
            elevator.opening()
            print(f'{person.passangers} {exit_message}')
            elevator.closing()

    else:
        while elevator.current_floor < person.target_floor:
            print(f'{elevator.current_floor}--{[person.passangers]}')
            sleep(1.2)
            elevator.elevator_up_side(1)

        if elevator.current_floor == person.target_floor:
            elevator.opening()
            print(f'{person.passangers} {exit_message}')
            elevator.closing()
    
