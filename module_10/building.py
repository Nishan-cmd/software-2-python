from elevator import Elevator
class Building:
    def __init__(self, no_of_bottom, no_of_top, no_of_elevators):
        self.no_of_bottom = no_of_bottom
        self.no_of_top = no_of_top
        self.elevators = [Elevator(no_of_bottom, no_of_top) for i in range(no_of_elevators)]

    def run_elevator(self, no_of_elevator, destination_floor):
        target_elevator = self.elevators[no_of_elevator - 1]
        print(f"The Elevator {no_of_elevator} is going to {destination_floor} floor.")
        target_elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Alarm Activated !!!!!!!!!!!!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.no_of_bottom)
        print(f"All elevator are at {self.no_of_bottom} floor below ground.")

