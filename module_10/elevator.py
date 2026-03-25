class Elevator:


    def __init__(self, no_of_bottom, no_of_top):
        self.no_of_bottom = no_of_bottom
        self.no_of_top = no_of_top
        self.on_floor = no_of_bottom

    def go_to_floor(self, floor_no):
        while self.on_floor < floor_no:
            self.floor_up()
        while self.on_floor > floor_no:
            self.floor_down()
        print(f"Elevator is at floor {self.on_floor}")

    def floor_up(self):
        self.on_floor += 1

    def floor_down(self):
        self.on_floor -= 1

