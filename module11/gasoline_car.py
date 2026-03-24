from car import Car


class Gasolinecar(Car):
    def __init__(self, new_reg_num, new_max_speed, tank_volume):
        super().__init__(new_reg_num, new_max_speed)
        self.tank_volume = tank_volume


gasolinecar = Gasolinecar("ACD-123", 165, 32.3)

gasolinecar.accelerate(150)
gasolinecar.drive(3)

print(gasolinecar.new_reg_num, gasolinecar.new_max_speed, "km/h", gasolinecar.tank_volume,"l" , gasolinecar.distance,"km")