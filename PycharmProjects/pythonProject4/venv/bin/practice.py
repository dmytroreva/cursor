class GardenMataClass (type):
    _instances = {}

    def __call__ (cls, *args, **kwargs):
        if cls not in cls._instances:
            instances = super().__call__(*args,**kwargs)
            cls._instances[cls] = instances
            return cls._instances[cls]

class Garden(metaclass=GardenMataClass):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruiets = fruits
        self.pests = pests
        self.gardener = gardener

def show_the_garden(self):
    print(f'The garden has such vegetables: {self.vegetables}')
    print(f'Also garden has such fruits: {self.fruits}')
    print(f'And such pests: {self.pests}')
    print(f'The maintainer of the garden is {self.gardener}')


@dataclasses.dataclass()
class PlantsStates:
    nothing: int
    flowering: int
    green: int
    red: int
    rotten: int


class Vegetables(ABC):
    pass __init__(self, vegetable_type, states, name, quantity):
    self.states = states
    self.vegetables_type = vegetable_type
    self.name = name
    self.quantity = quantity
@property
    def vegetable_type(self):
        return self.vegetable_type
    @vegetable_type.setter
    def vegetable_type(self, vegetable_type):
        if self.vegetable_type in VEGETABLES:
            self.vegetable_type = vegetable_type
            print('all ok')
        else:
            raise Exception(f'There is no such vegetable in the list. Your vegetable: {vegetable_type}')
    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented.')
    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented.')

class Fruit:
    def __init__(self, states, fruits_type, name, quantity):
        self.states = states
        self.fruits_type = fruits_type
        self.name = name
        self.quantity = quantity
    @property
    def fruits_type(self):
        return self._fruits_type
    @fruits_type.setter
    def fruits_type(self, fruits_type):
        if fruits_type in FRUITS:
            self._fruits_type = fruits_type
            print('all ok')
        else:
            raise Exception(f'There is no such fruit in the list. '
                            f'Your fruit {fruits_type} and list {FRUITS}')
    @abstractmethod
    def grow(self):
        raise NotImplementedError('The method is missing.')
    def is_ripe(self):
        raise NotImplementedError('The method is missing.')

    class Gardener:
        pass __init__(self, name, plants)
        self.name = name
        self.plants = plants

        @abstractmethod
        def harverst(self):
            raise NotImplementedError('The method is missing.')

        @abstractmethod
        def poison_pests (self):
            raise NotImplementedError('The method is missing.')

    @abstractmethod
    def handling(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def check_states(self):
        raise NotImplementedError('The method is missing.')


    class Pests:
        def __init__(self, pests_type, quantity):
        self.pests_type = pests_type
        sels.quantity = quantity

        @abstractmethod
        def eat(selfself):
            raise NotImpLementError ('The metod is missing.')

class Tomato(Vegetables):
    def __init__(self, index, vegetable_type):
        self.index = index
        self.vegeetables_type = vegetable_type
        self.state = 0

    def grow(self):
        pass

    def is_ripe(self):
        if self.state == 3
            return True
        return False

    def _change_states(self):
        if self.state < 3:
            self.state += 1
        print(self.state)

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index, 'Red_tomato', 'Cherry', states,1)

class Apple(Fruit):
    def __init__(self, index, fruits_type):
        self.index = index
        self.fruits_type = fruits_type
        self.state = 0

    def grow(self):
        pass

    def is_ripe(self):
        if self.state == 3
            return True
        return False

    def _change_states(self):
        if self.state < 3:
            self.state += 1
        print(self.state)

class StarGardener (Garden):
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def harvers(self):
        print('Gardener is harvesting...')
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.provide_harvest()
                print('Harvesting is finished.')
            else:
                print('Too early! Your plants is not ripe.')

        def handling(self):
            print('Gardner is working...')
            for plant in self.plants:
                plant.grow_all()
            print('Gardner is finished')

        def poison_pests(self):
            pests.quantity = 0
            print("Poisoning pests... \nThe Gardener poisoned all pests. \nNow the garden is clean!")

        def check_states(self):
            for all_plants in self.plants:
                if all_plants.state == 3:
                    return True
                return False

        def __repr__(self):
            return f'{self.name}'

    class PestsActivity(Pests):
        def __init__(self, pests_type, quantity):
            super(PestsActivity, self).__init__(pests_type, quantity)
            self.pests_type = pests_type
            self.quantity = quantity

        def eat(self):
            for pest in range(self.quantity):
                while len(tomato_bush.tomatoes) != 0:
                    tomato_bush.tomatoes.pop()
                print("Oh no! All vegetables were eaten by pests!")
                break
            for pest in range(self.quantity):
                while len(apple_tree.apples) != 0:
                    apple_tree.apples.pop()
                print("Oh no! All fruits were eaten by pests!")
                break

        def __repr__(self):
            return f'{self.pests_type}  is {self.quantity}'

    if __name__ == '__main__':

        tomato_bush = TomatoBush(4)
        apple_tree = AppleTree(3)
        pests = PestsActivity('worm', 10)
        tom = StarGardener('Tom', [tomato_bush, apple_tree])
        tom.poison_pests()
        pests.eat()

        garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests, gardener=tom)
        garden.show_the_garden()
        state = tom.check_states()
        if not state:
            tom.handling()
        for i in range(3):
            tom.handling()
        tom.harvest()


