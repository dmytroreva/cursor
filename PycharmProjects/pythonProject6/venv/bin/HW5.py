import dataclasses
import collections

class Laptop:
    def __init__(self, battery):
        self.battery = Battery(battery)
    def __str__(self):
        return f"This is a class Laptop with the battery {self.battery}."

class Battery:
    def __init__(self, mane=0):
        self.name = name
    def __str__(self):
        return f"{self.name}"

Laptop = Laptop("battery1")
print(Laptop)
print(laptop.battery)

class Guitar:
    def __init__(self, strings):
        self. strings = strings
    def __str__(self):
        return f"My guitar has {self.strings} strings."

class GuitarString:
    def __init__(self, num):
        self.num = num
    def __str__(self):
        return  f"{self.num}"

string = GuitarString(6)
guitar = string(string)
print(string)
print(guitar)

class Calc:

   @staticmethod
    def add_nums(a, b, c):
        return a + b + c

calc = Calc.add_nums(2, 3 ,5)
print(calc)

class Pasta:

    def __init__(self, ingradients):
        self.ingradients = ingradients

    @classmethod
    def Carbonara(cls):
        return Pasta (['forsmeat', 'tomatoes'])

    @classmethod
    def Bolognaise(cls):
        return Pasta(['bekon', 'parmesan','eggs'])

pasta_1 = Pasta (["tomato", "cucumber"])
pasta_2 = Pasta.bolognaise()

print(pasta_1.ingradients)
print(pasta_2.ingradients)

class Concert:
    def __init__(self, visitors_count=0):
        self.visitors.count = visitors_count

    @propertry
    def visitors_count(self):
        return self.visitors_count

    @visitors_count.setter
    def visitors_count (self,_visitors_count):
        if _visitors_count >= self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = _visitors_count

Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

@dataclasses.dataclass
class AddressBookDataclass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

ad_book1 = AddressBookDataClass(1, "Simon", "0991234567", "Kyiv", "simon@gmail.com", "15.05.1995", 25)
print(ad_book1)

AddressBookDataClass1 = collections.namedtuple("AddressBookDataClass1", ["key", "name", "phone_number", "address",
                                                                         "email", "birthday", "age"])
ad_book2 = AddressBookDataClass1(2, "Lia", "0992345678, "Lviv", "lia@gmail.com", "16.06.1996", 24)
print(ad_book2)

class AddressBook:

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"{__class__.__name__}(key={self.key}, name={self.name}, phone_number={self.phone_number}, " \
               f"address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})"


july = AddressBook(3, "July", "0993456789", "Kyiv", "july@gmail.com", "17.07.1997", 23)
print(july)

class Person:

    name = "John"
    age = 36
    country = "USA"


person = Person()
person.age = 40
print(person.age)

class Student:

    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(1, "SJ")
setattr(student, "email", "sj@gmail.com")
print(student.email)
student_email = student.__getattribute__("email")
print(getattr(student, "email"))
print(student_email)

class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


convert = Celsius(35)

print(f"Conversion is done! The temperature is {convert.temperature} F!")








