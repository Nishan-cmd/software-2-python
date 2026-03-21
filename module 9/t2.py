from car import Car

car = Car("AB-X", 500)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"The Current speed of the Car is {car.cur_speed} km/hr")
car.accelerate(-200)
print(f"The Current speed of the Car is {car.cur_speed} km/hr")