Elevator System Simulation
This project simulates an elevator system that interacts with passengers and manages their movement between floors. The code handles multiple passengers, ensures efficient movement, and provides detailed logs of the elevator's operations.

Features
Passenger Management:

The system interacts with two passengers, determining their current and target floors.
Passengers can enter and exit the elevator at the appropriate floors.
Elevator Movement:

The elevator moves up or down based on the passenger's current floor.
Stops at the required floors to pick up or drop off passengers.
Dynamic Messages:

Prints real-time information about the elevator's current floor and passenger activities.
Encapsulation:

Functions and classes are modular, making the system easy to extend.
Requirements
Python 3.12 or above.
The following modules/files:
elevator:
Includes the Elevator class and an instance named building_elevator.
passengers:
Includes the Passengers class and two instances: passenger_example_one and passenger_example_two.
move_with_passenger:
Manages passenger interactions after they enter the elevator.
back_settings.message_to_user:
Includes messages such as enter_message for passenger actions.
How to Use
Ensure all required files/modules are in the same directory as the main script.
Define passengers with their current_floor and target_floor in the Passengers class.
Define an elevator instance with its starting floor using the Elevator class.
Call the elevator_system() function, passing:
Two passenger objects.
The elevator object.