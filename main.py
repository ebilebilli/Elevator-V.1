from elevator import Elevator, building_elevator
from passengers import Passengers, passenger_example_one, passenger_example_two
from move_with_passenger import elevator_move_with_passenger
from back_settings.message_to_user import enter_message

def elevator_system(person_one: Passengers, person_two: Passengers, elevator: Elevator):
    print(f"Elevator floor: {elevator.current_floor}, "
          f"{person_one.passangers}: {person_one.current_floor} Target Floor: {person_one.target_floor}, "
          f"{person_two.passangers}: {person_two.current_floor} Target Floor: {person_two.target_floor}")
    
    if person_one.current_floor > elevator.current_floor or person_two.current_floor > elevator.current_floor:
        elevator.elevator_up_side(1)
        while elevator.current_floor < max(person_one.current_floor, person_two.current_floor):
            print(f"Elevator moving up: {elevator.current_floor}")
            elevator.elevator_up_side(1)
        elevator.opening()
        if elevator.current_floor == person_one.current_floor:
            print(f"{person_one.passangers} {enter_message}")
        if elevator.current_floor == person_two.current_floor:
            print(f"{person_two.passangers} {enter_message}")
        elevator.closing()
        elevator_move_with_passenger(person_one, person_two, elevator)

    elif person_one.current_floor < elevator.current_floor or person_two.current_floor < elevator.current_floor:
        elevator.elevator_down_side(1)
        while elevator.current_floor > min(person_one.current_floor, person_two.current_floor):
            print(f"Elevator moving down: {elevator.current_floor}")
            elevator.elevator_down_side(1)
        elevator.opening()
        if elevator.current_floor == person_one.current_floor:
            print(f"{person_one.passangers} {enter_message}")
        if elevator.current_floor == person_two.current_floor:
            print(f"{person_two.passangers} {enter_message}")
        elevator.closing()
        elevator_move_with_passenger(person_one, person_two, elevator)

    else:
        elevator.opening()
        print(f"{person_one.passangers} {enter_message}")
        elevator.closing()
        elevator_move_with_passenger(person_one, person_two, elevator)


elevator_system(person_one=passenger_example_one, person_two=passenger_example_two, elevator=building_elevator)
