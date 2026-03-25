from elevator import Elevator
from building import Building

Noika = Building(-2, 5, 4)

Noika.run_elevator(1,2)
Noika.run_elevator(2,5)
Noika.run_elevator(3,5)
Noika.run_elevator(4,2)


Noika.fire_alarm()