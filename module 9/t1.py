from car import Car

ford = Car("ABC-123", 142)

ford.accelerate(30)
ford.accelerate(70)
ford.accelerate(50)

print(ford.cur_speed)
ford.accelerate(-200)
print(ford.cur_speed)