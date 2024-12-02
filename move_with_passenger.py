from time import sleep
from elevator import Elevator
from passengers import Passengers
from back_settings.message_to_user import exit_message
from back_settings.system_clear import clear_screen


def elevator_move_with_passenger(person_one: Passengers, person_two: Passengers, elevator: Elevator):
    target_floors = sorted([person_one.target_floor, person_two.target_floor])

    for target in target_floors:
        while elevator.current_floor != target:
            if elevator.current_floor < target:
                print(f"{elevator.current_floor} -- {[person_one.passangers, person_two.passangers]}")
                sleep(1.2)
                elevator.elevator_up_side(1)
            else:
                print(f"{elevator.current_floor} -- {[person_one.passangers, person_two.passangers]}")
                sleep(1.2)
                elevator.elevator_down_side(1)

        elevator.opening()
        if elevator.current_floor == person_one.target_floor:
            print(f"{person_one.passangers} {exit_message}")
        if elevator.current_floor == person_two.target_floor:
            print(f"{person_two.passangers} {exit_message}")
        elevator.closing()
        sleep(1.2)
