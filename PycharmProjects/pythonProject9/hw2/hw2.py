from abc import abstractmethod, ABC

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    Perent class, should have eat. sleep
    """

    def eat(self):
        print(f"A(n) {self.__class__.__name__} called {self.name} is eating.")

    def sleep(self):
        print(f"A(n) {self.__class__.__name__}  called {self.name} is sleeping zzz....")


class Dog(Animal):
    def __init__(self, breed, name, age):
        super().__init__(name, age)
        self.breed = breed

    def breed_name(self):
        print(f" I am {self.breed} dog called {self.name}.")

class Goat(Animal):
    def milking(self):
        print(f"{self.name} the goat is being milked!")


class Horse(Animal):
    def __init__(self, colour, characteristics, name, age):
        super().__init__(name, age)
        self.colour = colour
        self.characteristics = characteristics

    def about_horse(self):
        print(f"I am a {self.characteristics} called {self.name}. My colour is {self.colour} and I am {self.age} y. o.")


class Shark(Animal):
    def swimming(self):
        print(f" {self.name} the shark is swimming")

    def hunting(self):
        print(f"{self.name} the shark is hounting")


class Lizard(Animal):
    def crawling(self):
        print(f"{self.name} the lizard is crawling carefully")

dog = Dog('Rain', 'Snow', 2)
goat = Goat('Bill', 4)
horse = Horse('black', 'pony', 'Power', 7)
shark = Shark('AJ', 5)
lizard = Lizard('Evan', 1)

dog.breed_name()
dog.eat()
goat.milking()
goat.sleep()
horse.about_horse()
shark.hunting()
shark.swimming()
lizard.crawling()

for item in (dog, goat, horse, shark, lizard):
    print(isinstance(item, Animal))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introducing(self):
        print(f" I am {self.name}. I am {self.age} y. o.")


class Centaur(Human, Animal):

    def running(self):
        print(f"{self.name} is running with other centaurs.")


centaur = Centaur('Charon', 50)

centaur.eat()
centaur.introducing()
centaur.running()

class Person:
    def __init__(self):
        arm1 = Arm("Beckoning")
        arm2 = Arm("Pointing")
        self.arms = [arm1, arm2]


class Arm:
    def __init__(self, gesture):
        self.gesture = gesture


person1 = Person()
for arm in person1.arms:
    print(arm.gesture)


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, display_type):
        self.display_type = display_type


screen = Screen('ELD')
cell_phone = CellPhone(screen)
print(screen.display_type)

class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.parameters = [name, last_name, phone_number, address, email,
                           birthday, age, sex]

    def __str__(self):
        return str(self.parameters)

class Laptop(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def screen(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def webcam(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def ports(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError("Your method is not implemented")



my_profile = Profile('Dmytro', 'Reva', '0992612334', 'Boryspilska str', 'revadise@gmail.com', '30.08.1996',
                     '24', 'Mr')
print(my_profile)


    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def core(self):
        raise NotImplementedError

class AcerES15(Laptop):
    def __init__(self, laptop_screen, laptop_keyboard, laptop_touchpad, laptop_webcam, laptop_ports, laptop_dynamics):
        self.laptop_screen = laptop_screen
        self.laptop_keyboard = laptop_keyboard
        self.laptop_touchpad = laptop_touchpad
        self.laptop_webcam = laptop_webcam
        self.laptop_ports = laptop_ports
        self.laptop_dynamics = laptop_dynamics

    def screen(self):
        print(f" The laptop's screen is {self.laptop_screen}")

    def keyboard(self):
        print(f"Laptop's keyboard is {self.laptop_keyboard}")

    def touchpad(self):
        print(f"Laptop's touchpad is {self.laptop_touchpad}")

    def webcam(self):
        print(f"Laptop's webcam is {self.laptop_webcam}")

    def ports(self):
        print(f"Laptop's ports are {self.laptop_ports}")

    def dynamics(self):
        print(f"Laptop's core are {self.laptop_dynamics}")


AcerES15 = HPLaptop('HD', 'without backlight', 'buttonless', '2 MP', 'USB 3.1', 'IntelCoreI5')

AcerES15.screen()
AcerES15.keyboard()
AcerES15.touchpad()
AcerES15.webcam()
AcerES15.ports()
AcerES15.core()
