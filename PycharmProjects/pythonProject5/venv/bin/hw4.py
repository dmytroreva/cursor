class Vehicle:
    def __init__(self, max_speed, mileage):
        self._max_speed = max_speed
        self._mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self._seting_capacity = seating_capacity
        self().__init__(max_speed, mileage)

    def get_seating_capacity(self):
        return self._seating_capacity


class School:
    def __init__(self, get_school_id, number_of_students):
        self._get_school_id = get_school_id
        self._number_of_students = number_of_students

class SchoolBus (School, Bus):
    def __init__(self, get_school_id, number_of_students):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)

    def bus_school_color(self, color):
        return self.bus_school_color


class Bear:
    def make_sound(self):
        return print("Bear sounds")

class Wolf:
    def make_sound(self):
        return print("Wolf sounds")


class City:

    def __init__(self, name, population):
        self._name = name
        self._population = population

    def __new__(cls, name, population):
        print("Creating Instance")
        instance = super(City, cls).__new__(cls)
        if population >= 1500:
            return instance
        else:
            return "Your city is to small"

   def __str__(self):
        return f'The population of the city {self._name} is {self._population}'


   def __add__(self, x):
        return self._population * x if x > 10 else self._population + x

class Count :
    def __init__(self, count):
     self.count = count

    def __add__(self, other):
         if self.count > 10 or other.count > 10:
             total_count = self.count * other.count
         else:
             total_count = self.count + other.count
         return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'

a = Count(50)
b = Count (5)
c = a + b
print (c)

a1 = Count(100)
b1 = Count(200)
c1 = a1 + b1
print (c1)


class MyOrder:
    def __init__(self, cart, custumer):
        self._cart = cart
        self._custumer = custumer

    def __bool__(self):
        return True if len(self._cart) != 0 else False

School_bus = Bus(4, 5, 6)
print(f'class of School_bus is {type(School_bus)}')

if isistance(School_bus, Vehicle):
    print('School_bus is also instance Vehicle')

bear = Bear()
wolf = Wolf()
for animals in bear, wolf:
    animals.make_sound()
'''7.Output:
Bear sounds
Wolf sounds'''

people_1 = City('Lviv', 10000)
print(people_1)
people_2 = City('Kyiv', 100)
if people_2:
    print(people_2)
'''8.;9.Output:
Creating Instance
City Lviv: 10000 population
Creating Instance
YOur city is too small'''

print("10.1", people_1 + 9)
print("10.2", people_1 + 11)
'''10. Output: 15

order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
''' 12. Output:
True
False'''