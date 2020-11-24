from collections import namedtuple
import json


Car = namedtuple('Car', 'color mileage car')
Pt = namedtuple('Pt', 'x y')

car = Car('red', {'123': 456}, Pt(1, (1,2,3,4,5)))
print(type(car))
print(isinstance(car, Car))
print(json.dumps(car._asdict()))
