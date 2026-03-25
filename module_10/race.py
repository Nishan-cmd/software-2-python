from car import Car
import random
import tabulate
class Race:
    def __init__(self, name, distance_KM, cars):
        self.name = name
        self.distance_KM = distance_KM
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        printable_cars = []
        for car in self.cars:
            printable_cars.append(car.get_info())
        table = tabulate.tabulate(printable_cars, headers="keys", tablefmt="fancy_grid")
        print(table)

    def race_finished(self):
        return any(car.distance >= self.distance_KM for car in self.cars)


class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, capacityKWH):
        Car.__init__(self, reg_num, max_speed)
        self.capacity_KWH = capacityKWH


class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, volume_L):
        Car.__init__(self, reg_num, max_speed)
        self.volume_L = volume_L