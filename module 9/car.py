class Car :
    def __init__(self, new_reg_num, new_max_speed ):
        self.reg_num = new_reg_num
        self.max_speed = new_max_speed
        self.cur_speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.cur_speed = self.cur_speed + change

        if  self.cur_speed < 0:
            self.cur_speed = 0

        #same check for max_speed
        if self.cur_speed > self.max_speed:
            self.cur_speed = self.max_speed

    def drive(self, hour):
        self.distance += self.cur_speed * hour

    def get_info(self):
        return {
            "reg_num": self.reg_num,
            "max_speed": self.max_speed,
            "cur_speed": self.cur_speed,
            "distance": self.distance
        }