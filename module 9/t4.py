from car import Car
import random
from tabulate import tabulate
cars = []
#create an empty list (cars)

#popuate list in a for loop that runs 10 times
#in the loop use "i" to create reg_num like "ABC-" +i
#use random library to set the max_speed
for i in range (10):
    reg_num = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    car = Car(reg_num, max_speed)
    cars.append(car)

race = True


#create variable  race = True
#accelerate and drive each car 1 hour (for in), accelerate first (random -15 to 10)
#check if distance of one of the cars >= 10000
#if so, race = false

while race:
    for car in cars:
        car.accelerate(random.randint(-15, 10))
        car.drive(1)
        if car.distance >= 10000:
            race = False

#print cars
printable_cars = []
for car in cars:
    printable_cars.append(car.get_info())
table = tabulate(printable_cars, headers="keys", tablefmt="fancy_grid")
print(table)