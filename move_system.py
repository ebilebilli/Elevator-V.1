from time import sleep
from elevator import Elevator
from passengers import Passengers
from back_settings.message_to_user import enter_message
from back_settings.system_clear import clear_screen


def elevator_system(person_one: Passengers, person_two: Passengers, elevator: Elevator):
    target_floors = sorted([person_one.current_floor, person_two.current_floor])
    direction = 1 if elevator.current_floor < target_floors[-1] else -1

    while elevator.current_floor != target_floors[-1]:
        elevator.current_floor += direction
        print(f"{elevator.current_floor} -- []")
        sleep(1.2)

    for target in target_floors:
        if elevator.current_floor == target:
            elevator.opening()
            if elevator.current_floor == person_one.current_floor:
                print(f"{person_one.passangers} {enter_message}")
            if elevator.current_floor == person_two.current_floor:
                print(f"{person_two.passangers} {enter_message}")
            elevator.closing()
            sleep(1.2)
