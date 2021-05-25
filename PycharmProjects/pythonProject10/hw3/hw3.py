from abc import ABC, abstractmethod
import random


class People(ABC):
    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_a_house(self, *args, **kwargs):
        pass


class Person(People):
    def __init__(self, name, age, money, home: list):
        self.name = name
        self.age = age
        self.money = money
        self.home = home

    def info(self):
        print(f"My name is {self.name}. I'm {self.age} years old.\n"
              f"I have ${self.money} in my wallet.")
        if len(self.home) >= 1:
            print(f"{self.name}: I have such realty: {self.home}.")
        else:
            print(f"{self.name}: I have no realty.")

    def make_money(self):
        print(f"{self.name}: I earned some money. \n"
              f"Now I have ${self.money} in my wallet.")
        self.money += random.randrange(200, 500, 100)

    def buy_a_house(self, house, realtor):
        if realtor.steal_money is True:
            self.money = 0
            print("Shit! The realtor stole my money!")

        if house in realtor.houses:
            if self.money >= house.cost:
                print(f"{self.name}: I buy the house {house.address} with area {house.area} sq.m. which costs"
                      f" ${house.cost}.")
                self.money -= house.cost
                print(f"{self.name}: Now I have ${self.money}.")
                self.home.append(house.address)
                realtor.sold_house(house)
            else:
                while self.money < house.cost:
                    print(f"Can't buy this house {house.address}. I must earn more money or choose another one.")
                    print("What should we do?\n")
                    action = input("Please input '1' for earning money or '2' for choosing another one': ")
                    if action == "1":
                        self.make_money()

                    else:
                       print("Incorrect action! Try again!")
        else:
            return "There is no houses available"


class Home(ABC):
    @abstractmethod
    def apply_a_purchase_discount(self, discount):
        raise NotImplementedError


class House(Home):
    def __init__(self, cost, area, discount):
        self.cost = cost
        self.area = area
        self.discount = discount

    def apply_a_purchase_discount(self, discount):
        if discount > 0:
            print(f"You're lucky! A discount for house {self.address} is {discount}!"
                  f"Now it costs {self.cost - round(self.cost * discount)}")
            self.cost -= round(self.cost * discount)
        else:
            print(f"Sorry, but there is no discount for house {self.address}.")


class SmallTypicalHouse(House):
    def __init__(self, address, cost, area=40):
        super().__init__(address, area, cost)


class RealtorMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):

    def __init__(self, name, houses: list, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_info_about_houses(self):
        if self.houses is not []:
            print(f"My name is {self.name} and I'm a realtor.\n"
                  f"{self.name}: There are such houses:")
            for house in self.houses:
                print(f"- {house.address} with {house.area} sq.m. which costs ${house.cost}")

        else:
            print("There is no houses on sale!")

    def give_a_discount(self, house):
        house.apply_a_purchase_discount(self.discount)

    def steal_money(self):
        i = random.randrange(1, 10)
        if i == 1:
            print(f"The realtor {self.name} steal your money!")
            return True

    def sold_house(self, house):
        self.houses.remove(house)


house1 = House("7441 West str", 200, 37000)
house2 = House("456 Main str", 150, 45210)
house3 = House("789 East str", 100, 30500)
house4 = SmallTypicalHouse("852 North str", 3750)
andy = Person("Andy", 35, 55000, [])
andy.info()
realtorr = Realtor("Dmytro", houses=[house1, house2, house3, house4], discount=round(random.uniform(0.05, 0.15), 2))
realtorr.steal_money()
realtorr.provide_info_about_houses()
realtorr.give_a_discount(house1)
andy.buy_a_house(house1, realtorr)
andy.info()
ivan = Person("Ivan", 30, 50000, ["123 Forest str"])
ivan.info()
realtorr.provide_info_about_houses()
realtorr.steal_money()
realtorr.give_a_discount(house2)
ivan.buy_a_house(house2, realtorr)
ivan.info()
davis = Person("David", 28, 10000, [])
david.buy_a_house(house4, realtorr)
david.info()