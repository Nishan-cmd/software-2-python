from car import Car

class ElectricCar(Car):
    def __init__(self, new_reg_num, new_max_speed, bat_capacity):
        super().__init__(new_reg_num, new_max_speed)
        self.bat_capacity = bat_capacity

electric_car = ElectricCar("ABC-15", 180, 52.5)

electric_car.accelerate(100)
electric_car.drive(3)
print(electric_car.new_reg_num, electric_car.distance,"km", electric_car.bat_capacity,"kWh")


